import json
import os
def lambda_handler(event, context):
	command="echo " + event['queryStringParameters']['name']
    cmd_result = os.popen(command).read()
    return {
    	"statusCode": 200,
    	"body": json.dumps(cmd_result)
    }