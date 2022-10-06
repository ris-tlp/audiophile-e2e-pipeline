# resource "aws_redshift_cluster" "audiophile_cluster" {
#   cluster_identifier = "tf-redshift-cluster"
#   database_name      = "crinacle_audiophile_ratings"
#   master_username    = "admin"
#   master_password    = var.redshift_password
#   node_type          = "dc2.large"
#   cluster_type       = "single-node"

#   skip_final_snapshot                 = true
#   publicly_accessible                 = true
#   automated_snapshot_retention_period = 0
#   vpc_security_group_ids              = [aws_security_group.redshift_security_group.id]
# }

# resource "aws_security_group" "redshift_security_group" {
#   name = "redshift_security_group"
#   ingress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }
