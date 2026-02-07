terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
  # If using access keys, add here (not recommended)
  # access_key = var.access_key
  # secret_key = var.secret_key
}
