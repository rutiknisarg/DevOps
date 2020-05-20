#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

##############################################################################
# Owner : Rutik Nisarg Samal
# Email : rutiknisarg@gmail.com
# Description: This script will list all the EBS volumes across all the the acounts linked to AWS Organization across all the regions.
# Command to Execute: python3 awsebs.py
##############################################################################

import boto3
import awsOrganization
import awsAllRegions

aws_all_region_list = awsAllRegions.get_all_regions()
aws_account_list = awsOrganization.all_aws_accounts()

aws_region_with_no_ebs_vol = set()
aws_region_restricted_list = set()

def get_all_ebs_volume():
    print("Account Name", "|",  "Region   ", "|", "EC2 Instance ID    ", "|", "EBS Volume ID        ", "|", "Mount Name", "|", "State")
    print("---------------------------------------------------------------------------------------------------------------------------")
    for account in aws_account_list:
        session = boto3.Session(profile_name=str(account[0]), region_name=None)
        for region in aws_all_region_list:
            ec2_client = session.client(service_name='ec2', region_name=region)
            try:

                volumes = ec2_client.describe_volumes()
                if len(volumes['Volumes']) == 0:
                    aws_region_with_no_ebs_vol.add(region)
                else:
                    for vol in volumes['Volumes']:
                        if vol['Attachments'] == []:
                            print(account[0], "|",  region, "|", "Not attached to any Instance", "|", vol['VolumeId'], "|", "Not mounted", "|", "Not attached")
                        else:
                            print(account[0], "|", region, "|", vol['Attachments'][0]['InstanceId'], "|", vol['Attachments'][0]['VolumeId'], "|", vol['Attachments'][0]['Device'], "|", vol['Attachments'][0]['State'])

            except:
                aws_region_restricted_list.add(region)


get_all_ebs_volume()
# print("List Of Regions Where No EBS Volume Present: ", aws_region_with_no_ebs_vol)
# print("\n")
# print("List Of Regions Where Resource Creation is restricted: ", aws_region_restricted_list)
# print("\n")
