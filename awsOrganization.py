#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

##############################################################################
# Owner : Rutik Nisarg Samal
# Email : rutiknisarg@gmail.com
# Description: This script will list all the acounts linked to yiur AWS Organization.
# Command to Execute: python3 awsOrganization.py
##############################################################################

import boto3

session = boto3.Session(profile_name=None, region_name=None)
client = boto3.client('organizations')
response = client.list_accounts()

def all_aws_accounts():
    aws_account_list = []

    for account in response['Accounts']:
        aws_account_id = account['Id']
        aws_account_email = account['Email']
        aws_account_name = account['Name']
        aws_account_status = account['Status']

        aws_single_account_info = [aws_account_id, aws_account_email, aws_account_name, aws_account_status]
        aws_account_list.append(aws_single_account_info)

    return aws_account_list
