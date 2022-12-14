# Running this project

### Requirements

* cdktf 0.13+
* pipenv 2022.11.25+
* python 3.7+

### Install dependencies

```bash
 > cdktf provider add "aws@~>4.0"
 > pipenv install inquirer cdktf-cdktf-provider-aws
```

### Synth terraform

```bash
 > pipenv run python main.py 
 
[?] What size of machines do you need?: micro
   nano
 > micro
   small
   medium
   large

[?] Which regions should these instances be deployed?: 
   [ ] us-east-1
   [X] us-east-2
   [ ] us-west-1
 > [X] us-west-2

[?] Which action would you like to take?: apply
 > apply
   destroy

Synth completed successfully!

To create resources run: cdktf deploy --app "echo skipping-synth" prod-us-west-2 prod-us-east-2 --auto-approve

To delete resources run: cdktf destroy --app "echo skipping-synth" prod-us-west-2 prod-us-east-2 --auto-approve

```

> **_NOTE:_**  CDKTF currently doesn't support creating workspaces, they need to pre-exist in Terraform Cloud already with AWS credentials attached either as variables or [variable sets](https://developer.hashicorp.com/terraform/tutorials/cloud/cloud-multiple-variable-sets)

### Deploy stacks

```bash
 > cdktf deploy --app "echo skipping-synth" prod-us-east-2 prod-us-west-2 --auto-approve
```

### Destroy stacks

```bash
 > cdktf destroy --app "echo skipping-synth" prod-us-east-2 prod-us-west-2 --auto-approve
```