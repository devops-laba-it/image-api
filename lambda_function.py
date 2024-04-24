import base64
import os

import boto3

AWS_ACCESS_KEY_ID = os.environ.get('BOOKS_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('BOOKS_AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('BOOKS_AWS_REGION')
BUCKET_NAME = os.environ['BUCKET_NAME']

s3_client = boto3.client(
    service_name='s3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def lambda_handler(event, context):
    print(event)

    raw_path = event['rawPath']
    raw_path = raw_path.replace("/", "")

    print("raw_path", raw_path)
    try:
        response = s3_client.get_object(
            Bucket=BUCKET_NAME,
            Key=raw_path,
        )


        image = response['Body'].read()
        return {
            'headers': {"Content-Type": "image/png"},
            'statusCode': 200,
            'body': base64.b64encode(image).decode('utf-8'),
            'isBase64Encoded': True
        }
    except s3_client.exceptions.NoSuchKey as e:
        print(e)
        return {
            'statusCode': 404,
            'body': 'Not found'
        }
