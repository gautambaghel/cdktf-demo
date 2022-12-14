#!/usr/bin/env python
import os
import inquirer
import subprocess
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance

class Ec2Stack(TerraformStack):
    def __init__(self, scope: Construct, id: str, name: str, provider_region: str, region_ami: str, instance_type: str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(self, id, region = provider_region)
        ec2 = Instance(self, "compute", ami = region_ami, instance_type = instance_type, tags={"Name": name},)

# ask machine size
size = [
inquirer.List('size',
              message="What size of machines do you need?",
              choices=['nano', 'micro', 'small', 'medium', 'large'],
          ),
]
size_answer = inquirer.prompt(size)

# ask region
all_regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
all_amis = ['ami-09d3b3274b6c5d4aa', 'ami-0beaa649c482330f7', 'ami-0f5e8a042c8bfcd5e', 'ami-0d593311db5abb72b']

regions = [
  inquirer.Checkbox('regions',
                    message="Which regions should these instances be deployed?",
                    choices=all_regions,
                    carousel=True
                    ),
]
regions_answers = inquirer.prompt(regions)

# ask terraform apply/destroy
action = [
inquirer.List('action',
              message="Which action would you like to take?",
              choices=['apply', 'destroy'],
          ),
]
action_answer = inquirer.prompt(action)

# initilize App
app = App()
for region in regions_answers["regions"]:
  name = "prod-" + region
  instance_type = "t2." + size_answer["size"]
  index = all_regions.index(region)
  stack = Ec2Stack(app, id=name, name=name, provider_region=region, region_ami=all_amis[index], instance_type=instance_type)
  CloudBackend(stack,
    hostname='app.terraform.io',
    organization='tfc-integration-sandbox',
    workspaces=NamedCloudWorkspace(name)
  )

# synthesize App
app.synth()

# do manual Terraform Apply
for region in regions_answers["regions"]:
  name = "prod-" + region
  init_tf = subprocess.run(["terraform", "-chdir=cdktf.out/stacks/"+name, "init"])
  run_tf = subprocess.run(["terraform", "-chdir=cdktf.out/stacks/"+name, str(action_answer["action"]), "-auto-approve"])