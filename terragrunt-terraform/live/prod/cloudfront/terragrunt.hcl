terraform {
  source = "../../../modules/cloudfront"
}

inputs = {
  bucket_name = "p81-dani-s3-bucket"
  tags = {
    Name        = "DaniP81Project"
    Owner       = "Dani Birman"
    Environment = "Prod"
    Terraform   = "True"
  }
}

include "root" {
  path = find_in_parent_folders()
}
