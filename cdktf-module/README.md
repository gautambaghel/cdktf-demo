# To use module in CDKTF

1. Initialize your CDKTF project as usual
2. Open cdktf.json file
3. add the module name on `terraformModules` array, for example: `terraform-aws-modules/vpc/aws@2.77.0`
4. run `cdktf get`