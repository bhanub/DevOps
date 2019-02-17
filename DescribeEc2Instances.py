# Describe Ec2 Instances From all the regions

import json
import boto3

def handler(event, context):

    client = boto3.client('ec2')
    response = client.describe_instances()
    responsetostr = json.dumps(response, indent=4, sort_keys=True, default=str)
    jsonresponse = json.loads(responsetostr)
    #return(jsonresponse)
    return describe_instances_from_anotheraccount()
    
def describe_instances_from_anotheraccount():
    sts_connection = boto3.client('sts')
    role_arn='arn:aws:iam::702599132502:role/CrossAccountEC2Access'  #Inline policy role
    role_session_name='test_cross_account_session'
    response=sts_connection.assume_role(
        RoleArn=role_arn,
        RoleSessionName=role_session_name
        )
    #responsetostr = json.dumps(response, indent=4, sort_keys=True, default=str)
    #jsonresponse = json.loads(responsetostr)
    #return(jsonresponse)
    sts_assumed_role = boto3.client('ec2',
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'],
        region_name='us-east-1'
        )
    response_instances = sts_assumed_role.describe_instances()
    responsetostr = json.dumps(response_instances, indent=4, sort_keys=True, default=str)
    jsonresponse = json.loads(responsetostr)
    return jsonresponse