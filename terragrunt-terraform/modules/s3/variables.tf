variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}


variable "oai_id" {
  description = "The ID of the CloudFront Origin Access Identity"
  type        = string
}

variable "tags" {
  description = "Tags to assign my project"
  type        = map(string)
}