resource "aws_instance" "mca_ec2" {
  ami           = "ami-04233b5aecce09244"
  instance_type = "t3.micro"

  tags = {
    Name = "MCA-MultiCloud-EC2"
  }
}
