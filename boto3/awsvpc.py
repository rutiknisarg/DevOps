#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

##############################################################################
# Owner : Rutik Nisarg Samal
# Email : rutiknisarg@gmail.com
# Description: This script will list all the VPCs across all the the acounts linked to AWS Organization across all the regions.
# Command to Execute: python3 awsvpc.py
##############################################################################

import boto3
import awsOrganization
import awsAllRegions

aws_all_region_list = awsAllRegions.get_all_regions()
aws_account_list = awsOrganization.all_aws_accounts()

aws_region_with_no_ebs_vol = set()
aws_region_restricted_list = set()

def get_all_vpc():
    for account in aws_account_list:
        session = boto3.Session(profile_name=str(account[0]), region_name=None)
        for region in aws_all_region_list:
            ec2_client = session.client(service_name='ec2', region_name=region)
            try:
                vpc_list = ec2_client.describe_vpcs()
                for vpc in vpc_list['Vpcs']:
                    print(account[0], vpc['CidrBlock'], vpc['VpcId'], vpc['State'], vpc['InstanceTenancy'], vpc['IsDefault'])
            except:
                aws_region_restricted_list.add(region)

get_all_vpc()

# print("List Of Regions Where No EBS Volume Present: ", aws_region_with_no_ebs_vol)
print("\n")
print("List Of Regions Where Resource Creation is restricted: ", aws_region_restricted_list)
print("\n")
