#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, provider_region: str, region_ami : str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(self, id, region = provider_region)
        ec2 = Instance(self, "my-instance" + provider_region, ami = region_ami, instance_type ="t2.small")

app = App()

MyStack(app, "prod-us-east-1", "us-east-1", "ami-09d3b3274b6c5d4aa")
MyStack(app, "prod-us-west-2", "us-west-2", "ami-0d593311db5abb72b")

app.synth()
