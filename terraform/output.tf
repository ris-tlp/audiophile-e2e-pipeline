# Output Region set for AWS
output "aws_region" {
  description = "Region set for AWS"
  value       = var.aws_region
}

output "bucket_name" {
  description = "S3 bucket name."
  value       = aws_s3_bucket.audiophile-bucket.id
}

output "redshift_password" {
  description = "Password for the database in the Redshift cluster"
  value       = var.redshift_password
}

output "redshift_user" {
  description = "Username for the database in the Redshift cluster"
  value       = aws_redshift_cluster.audiophile_cluster.master_username
}

output "redshift_port" {
  description = "Port of the database in the Redshift cluster"
  value       = aws_redshift_cluster.audiophile_cluster.port
}

output "redshift_host" {
  description = "Host to connect to the Redshift cluster"
  value       = aws_redshift_cluster.audiophile_cluster.endpoint
}

output "redshift_database" {
  description = "Database name in the Redshift cluster"
  value       = aws_redshift_cluster.audiophile_cluster.database_name
}
