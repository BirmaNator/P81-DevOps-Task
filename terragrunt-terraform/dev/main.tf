module "cloudfront" {
  source      = "../modules/cloudfront"

  bucket_name = var.bucket_name
  tags        = var.tags
}

module "s3" {
  source      = "../modules/s3"
  bucket_name = var.bucket_name
  tags        = var.tags
  oai_id      = module.cloudfront.oai_id
}

