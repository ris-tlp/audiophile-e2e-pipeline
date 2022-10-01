# Create S3 bucket with a specific prefix
resource "aws_s3_bucket" "audiophile-bucket" {
  bucket_prefix = var.bucket_prefix
  force_destroy = true
}

# Enable versioning for S3 bucket
resource "aws_s3_bucket_versioning" "audiophile-bucket-versioning" {
  bucket = aws_s3_bucket.audiophile-bucket.id
  versioning_configuration {
    status = var.versioning
  }
}
