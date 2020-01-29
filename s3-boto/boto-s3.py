import json
import boto3
import os

s3_client = boto3.client('s3',
  aws_access_key_id=os.environ.get('ACCESS_KEY', 'invalid'),
  aws_secret_access_key=os.environ.get('SECRET_KEY', 'invalid'),
  region_name='sa-east-1',
)

response = s3_client.list_buckets()
buckets = response.get('Buckets')

for bucket in buckets:

  print(bucket)


s3 = boto3.resource('s3',
  aws_access_key_id=os.environ.get('ACCESS_KEY', 'invalid'),
  aws_secret_access_key=os.environ.get('SECRET_KEY', 'invalid'),
  region_name='sa-east-1'
)

bucketObj = s3.Bucket('blackdevs-aws')
for obj_sum in bucketObj.objects.all():
  obj = s3.Object(obj_sum.bucket_name, obj_sum.key)
  print(obj)


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.loads('{"message": "OK"}')
    }