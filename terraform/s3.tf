resource "aws_s3_bucket" "audiophile-bucket" {
  bucket_prefix = var.bucket_prefix
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "audiophile-bucket-versioning" {
  bucket = aws_s3_bucket.audiophile-bucket.id
  versioning_configuration {
    status = var.versioning
  }
}
