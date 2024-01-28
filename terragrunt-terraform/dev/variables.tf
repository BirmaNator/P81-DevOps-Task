variable "bucket_name" {
  description = "The name of the S3 bucket for production"
  type        = string
}

variable "region" {
  description = "The region to create resources in it"
  type        = string
  default     = "us-east-1" # No particular reason for that to be default
}

variable "tags" {
  description = "Tags to assign my project"
  type        = map(string)
}
