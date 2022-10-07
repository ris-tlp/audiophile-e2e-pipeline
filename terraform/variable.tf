variable "aws_region" {
  description = "Region for the AWS services to run in."
  type        = string
  default     = "us-east-1"
}

variable "bucket_prefix" {
  description = "Bucket prefix for the S3"
  type        = string
  default     = "audiophile-e2e-pipeline-"
}

variable "rds_password" {
  description = "Password for the database in the RDS cluster"
  type        = string
}

variable "redshift_password" {
  description = "Password for the database in the Redshift cluster"
  type        = string
}

variable "versioning" {
  type    = string
  default = "Enabled"
}
