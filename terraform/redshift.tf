resource "aws_redshift_cluster" "audiophile_cluster" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = "crinacle_audiophile_ratings"
  master_username    = "admin"
  master_password    = var.redshift_password
  node_type          = "dc2.large"
  cluster_type       = "single-node"

  skip_final_snapshot                 = true
  publicly_accessible                 = true
  automated_snapshot_retention_period = 0
}
