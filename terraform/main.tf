resource "aws_instance" "my_instance" {
  ami           = "ami-0d593311db5abb72b"
  instance_type = "t2.small"
}