# EC2reporter

Inventory EC2 instances across all regions and produce a JSON output

## Example output

```json
[
  {
    "AvailabilityZone": "us-east-1a",
    "ImageId": "ami-afe051d7",
    "InstanceId": "i-0a6802b216c4b7499",
    "InstanceType": "c4.8xlarge",
    "KeyName": "mykey",
    "LaunchTime": "2018-02-02 22:51:15+00:00",
    "Name": "server1",
    "Owner": "dept1",
    "PrivateIpAddress": "172.17.65.200",
    "PublicIpAddress": "",
    "Region": "us-west-2",
    "State": "stopped",
    "SubnetId": "subnet-a95a0e99",
    "TechnicalContact": "dept1@test.com",
    "VpcId": "vpc-ea725699"
  },
  {
    "AvailabilityZone": "us-west-2a",
    "ImageId": "ami-b94cb0c1",
    "InstanceId": "i-00ab9424f65affd99",
    "InstanceType": "m4.xlarge",
    "KeyName": "discovery-key",
    "LaunchTime": "2017-10-23 21:24:10+00:00",
    "Name": "server2",
    "Owner": "dept2",
    "PrivateIpAddress": "172.17.112.99",
    "PublicIpAddress": "",
    "Region": "us-west-2",
    "State": "running",
    "SubnetId": "subnet-233b2399",
    "TechnicalContact": "dept2@test.com",
    "VpcId": "vpc-ea725699"
  },
  {
    "AvailabilityZone": "us-west-2a",
    "ImageId": "ami-ae60eece",
    "InstanceId": "i-0142392fb666799",
    "InstanceType": "t2.small",
    "KeyName": "mykey",
    "LaunchTime": "2017-03-14 20:20:55+00:00",
    "Name": "server4",
    "Owner": "dept4",
    "PrivateIpAddress": "172.20.17.99",
    "PublicIpAddress": "",
    "Region": "us-west-2",
    "State": "stopped",
    "SubnetId": "subnet-20b84399",
    "TechnicalContact": "dep4@test.com",
    "VpcId": "vpc-bf028099"
  } 
]
```