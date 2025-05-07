resource "aws_budgets_budget" "monthly_cost" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = "20.0"
  limit_unit        = "USD"
  time_unit         = "MONTHLY"
  time_period_start = "2025-01-01_00:00"

  cost_filter {
    name   = "Service"
    values = ["AmazonEC2"]  # You can filter by EC2 service here
  }
}
