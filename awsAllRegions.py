#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

##############################################################################
# Owner : Rutik Nisarg Samal
# Email : rutiknisarg@gmail.com
# Description: This script will list all the regions available in your AWS account(AWS).
# Command to Execute: python3 awsAllRegions.py
##############################################################################

import boto3

session = boto3.Session(profile_name=None, region_name=None)
ec2_client = session.client(service_name='ec2')
all_regions = ec2_client.describe_regions()

def get_all_regions():
    aws_all_region_list = []
    for region_name in all_regions['Regions']:
        aws_all_region_list.append(region_name['RegionName'])
    return aws_all_region_list
