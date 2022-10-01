variable "aws_region" {
  description = "Region for the AWS services to run in."
  type        = string
}

variable "bucket_prefix" {
  description = "Bucket prefix for the S3"
  type        = string
  default     = "audiophile-e2e-pipeline-"
}

variable "versioning" {
  type    = string
  default = "Enabled"
}
