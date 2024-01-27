output "oai_id" {
  value = aws_cloudfront_origin_access_identity.oai.id
}

output "cloudfront_url" {
  value = aws_cloudfront_distribution.s3_distribution.domain_name
}