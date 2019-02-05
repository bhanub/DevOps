# Describe Ec2 Instances

import json
import boto3

def handler(event, context):

    client = boto3.client('ec2')
    response = client.describe_instances()
    responsetostr = json.dumps(response, indent=4, sort_keys=True, default=str)
    jsonresponse = json.loads(responsetostr)
    return(jsonresponse)