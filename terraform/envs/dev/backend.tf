terraform {
  backend "s3" {
    bucket         = "gitops-tf-state-nagarjuna-001"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
