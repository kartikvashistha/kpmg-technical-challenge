# kpmg-technical-challenge

## Challenge 1

Simple 3 Tier app deployment via Terraform on the Azure Cloud. The infrastructure setup is as follows:

1) 1 Load balancer for the front end web server()
2) 1 front end web server (Windows VM)
3) 1 Internal Load balancer
4) 1 backend Linux VM
5) A database and databse server

### Prerequisites
1) Have Terraform installed
2) Logged in to your Azure account on cli via `az-cli`

### Run instructions
To deploy the infrastructure on Azure, run the following commands:
```
terraform init
terraform plan
terraform apply
```

To undeploy the resources, run the following:
```
terraform destroy
```


## Challenge 2

To view the metadata of a given instance( VM in the case of Azure) in JSON, run the `metadata.py` script **inside** the VM you want metadata from. You can also run the script with a key whose value you want in the JSON output.

---
**NOTE**

 This script was tested to work inside of a linux vm.

---

### Run instructions

To get the entire JSON, the code can be run as:

```
python metadata.py
```

To search the json for a key value:

```
python metadata.py name
```


In a Windows vm, you can obtain all of the metadata by running the following command in Powershell:
```
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -NoProxy -Uri "http://169.254.169.254/metadata/instance/compute/vmId?api-version=2017-08-01&format=text"
```


## Challenge 3

Problem statement:

object = {“x”:{“y”:{“z”:”a”}}}

key = x/y/z

value = a

To test the python function written to achieve this, run
```
python testgetValue.py
```
