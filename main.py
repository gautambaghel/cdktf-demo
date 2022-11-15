#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(self, "AWS", region="us-west-1")

        instance = Instance(self, "compute",
                            ami="ami-01456a894f71116f2",
                            instance_type="t2.micro",
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )

app = App()
stack = MyStack(app, "learn-cdktf")

CloudBackend(stack,
  hostname='app.terraform.io',
  organization='tfc-integration-sandbox',
  workspaces=NamedCloudWorkspace('learn-cdktf')
)

app.synth()
