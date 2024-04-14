from flask import Flask, request, render_template
from back import get_data
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, generate_latest
from datetime import datetime
import socket
import logging


cities_metric = Counter('cities', 'Cities view', ['city_input'])

app = Flask(__name__, static_url_path='/static')  # initialize flask app

# Configure Flask logging
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('app.log')  # Log to a file
app.logger.addHandler(handler)


metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')


@app.route("/", methods=['POST', 'GET'])
def home():
    c_id = socket.gethostname()
    app.logger.critical(f'TIME: {datetime.now()} host name:  {c_id} ')

    if request.method == 'POST':
        city_input = request.form['user_input']
        cities_metric.labels(city_input=city_input).inc()
        
        weather_data = get_data(city_input)
        if weather_data == 404 or weather_data == "Bad API response!":
            app.logger.error(f'TIME: {datetime.now()} BAD API RESPONSE in city {city_input} ')
            return render_template('error.html', err=weather_data)

        return render_template('index.html', weather_data=weather_data, c_id=c_id)
    return render_template('index.html', c_id=c_id)

@app.errorhandler(404)
def unknown_page(err):
    return render_template('error.html', error=err), 404
    
    
@app.route("/metrics")
def metrics():
    return generate_latest()
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
