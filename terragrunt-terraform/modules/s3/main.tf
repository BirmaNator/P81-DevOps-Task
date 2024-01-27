resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.bucket.bucket

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "s3:GetObject"
        Effect    = "Allow"
        Resource  = "arn:aws:s3:::${var.bucket_name}/*"
        Principal = {"AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity ${var.oai_id}"}
      },
    ]
  })
}