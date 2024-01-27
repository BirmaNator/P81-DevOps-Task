terraform {
  backend "s3" {
    bucket         = "p81-dani-tf-state-s3-bucket"
    key            = "terraform/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
