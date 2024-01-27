provider "aws" {
  region  = var.region
  version = "~> 5.33.0"
  # It is essential to use environment variables/secrets/secure way to inject Access key & Access Secret
}
