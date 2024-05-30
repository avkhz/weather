variable "key_name" {
  default = "dovekey"
}

variable "file_name" {
  default = "dovekey.pem"
}

variable "pub_key_name" {
  default = "dovekey.pub"
}

variable "region" {
  default = "eu-north-1"
}

variable "cluster_name" {
  default = "avihu_cluster"
}

variable "ami" {
  default = "ami-0705384c0b33c194c"
}

variable "worker_node_ec2_type" {
  default = "t3.small"
}
