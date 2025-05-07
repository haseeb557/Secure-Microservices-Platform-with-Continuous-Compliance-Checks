
output "vpc_id" {
  value = module.vpc.vpc_id
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.app_bucket.id
}
