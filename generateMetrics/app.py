
from typing import Dict, Any
import boto3
import random
import json 

NAMESPACE= 'InsuranceApplication'
METRIC_NAME= 'HealthCheck'
DIMENSION= 'Application'
REGION = 'us-east-1'

cloudwatch = boto3.client('cloudwatch', region_name=REGION)
application  = ['Region_1', 'Region_2']

def lambda_handler(event: Dict, context: Any) -> Dict:
    """lambda entry point for processing incoming event
    """

    try:

        cloudwatch.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[
            {
                'MetricName': METRIC_NAME,
                'Dimensions': [
                    {
                        'Name': DIMENSION,
                        'Value': random.choice(application)
                    },
                ],
                'Value': random.choice([0, 1]),
                'Unit': 'Count'
            },
        ]
    )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": " The metrics was pushed to cloudWatch",
              
            }),
        }
    except Exception as e:    
       
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error pushing the metrics to cloud watch ",
                "error": str(e)
                
            }),
        }