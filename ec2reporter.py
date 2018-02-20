#!/usr/bin/env python3
"""
Provides an JSON inventory of all EC2 instances running across all AWS regions.
"""

import json
import os
import boto3  


def main():
    instances = []
    printer = []
    for region in get_regions():
        instances.extend(get_instances(region))
    objects = create_objects(instances)
    for i in objects:
        printer.append(i.toJSON())
    print("[\n",',\n'.join(printer),"\n]")
    

def get_regions():
    """
    get and return a list of all current AWS regions
    """
    regions = []
    ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    response = ec2.describe_regions()
    for region in response['Regions']:
        regions.append(region['RegionName']) 
    return(regions)

def get_instances(region):
    """
    get and return a list of all instances in the provided region
    """
    instances = []
    ec2client = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(instance)
    return(instances)


def removebadchars(token):
    """
    Remove any undesirable characters that might gum up the works
    """
    translate = {'$': '', '&': '', '#': '', '*': '', '(': '', ')': '', '[': '', ']': '', ' ': '',
                '?': '','^': '', '`': '', '~': '', '{': '', '}': '', ',': '', '|': '', ':': '', ';': '', "'": '', '"': ''}
    for char in translate:
        token = token.replace(char, translate[char])
    return(token)

def create_objects(instances):
    """
    Create and object for each of the instances in the provided list and return a list of instance objects
    populated with the corresponding AWS and custom tag metadata.
    """
    objects = []
    for instance in instances:
        i  = Instance()
        i.AvailabilityZone = instance["Placement"]["AvailabilityZone"]
        i.InstanceId = instance["InstanceId"]
        i.InstanceType = instance["InstanceType"]
        i.State = instance["State"]["Name"]
        i.ImageId = instance["ImageId"]
        i.LaunchTime = str(instance["LaunchTime"]) 
        i.Region = i.AvailabilityZone[0:-1] 
        try:
            i.PrivateIpAddress = instance["PrivateIpAddress"]
        except:
            i.PrivateIpAddress = ""
        try:
            i.KeyName = instance["KeyName"].lower().replace(' ', '')
        except:
            i.KeyName = ""
        try:
            i.PublicIpAddress = instance["PublicIpAddress"]
        except:
            i.PublicIpAddress = ""
        try:
            i.SubnetId = instance["SubnetId"]
        except:
            i.SubnetId = ""
        try:
            i.VpcId = instance["VpcId"]
        except:
            i.VpcId = ""

        for tag in instance["Tags"]:
            if tag['Key'].lower() == 'owner':
                i.Owner = removebadchars(tag['Value'].lower()) 
            elif tag['Key'].lower() == 'name':
                i.Name = removebadchars(tag['Value'].lower())
            elif tag['Key'].lower() == 'technical_contact':
                i.TechnicalContact = removebadchars(tag['Value'].lower())
         
        if not "TechnicalContact" in i.__dict__:
            i.TechnicalContact = ''
        if not "Owner" in i.__dict__:
            i.Owner = ''
        if not "Name" in i.__dict__:
            i.Name = ''
        
        objects.append(i)

    return(objects)


class Instance:
    """
    Instance class to bind all AWS properties to
    """
    def toJSON(self):
        return(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))

if __name__ == "__main__":
    region_name='us-west-2'
    aws_access_key_id='**********'
    aws_secret_access_key='**************'
    main()
