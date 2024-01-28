terraform {
  source = "../../../modules/s3"
}

dependency "cloudfront" {
  config_path = "../cloudfront"
  }

inputs = {
    bucket_name = "p81-dani-s3-bucket"
    oai_id = dependency.cloudfront.outputs.oai_id
    tags        = {
      Name        = "DaniP81Project"
      Owner       = "Dani Birman"
      Environment = "Prod"
      Terraform   = "True"

    }
}


include "root" {
  path = find_in_parent_folders()
}
