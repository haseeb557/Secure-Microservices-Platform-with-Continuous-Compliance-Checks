resource "aws_security_group" "rds_sg_rds" {  # Changed the name here
  name        = "${var.project_name}-rds-sg"
  description = "Security Group for RDS"
  vpc_id      = module.vpc.vpc_id
}

resource "aws_db_subnet_group" "rds" {
  name       = "${var.project_name}-rds-subnet"
  subnet_ids = module.vpc.private_subnets
}

resource "aws_db_instance" "main" {
  identifier            = "${var.project_name}-db"
  engine                = "postgres"
  instance_class        = "db.t3.micro"
  allocated_storage     = 20
  username              = "dbadmin"
  password              = "StrongPassw0rd123!"
  db_subnet_group_name  = aws_db_subnet_group.rds.name
  vpc_security_group_ids = [aws_security_group.rds_sg_rds.id]  # Use the renamed security group
  skip_final_snapshot   = true
  multi_az              = false
  storage_type          = "gp2"
  publicly_accessible   = false
}

# If you're using Secrets Manager for password management:
data "aws_secretsmanager_secret" "db" {
  name = "db-password"
}

data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = data.aws_secretsmanager_secret.db.id
}

