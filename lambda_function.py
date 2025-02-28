import boto3
import csv
import uuid

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('vegeta-csv')

def lambda_handler(event, context):
    # Get bucket and file details from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Fetch the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8').splitlines()
    
    # Read CSV file
    reader = csv.DictReader(content)
    
    for row in reader:
        # Generate a unique ID for each record
        row['viji'] = str(uuid.uuid4())  

        # Insert data into DynamoDB
        table.put_item(Item=row)

    return {
        'statusCode': 200,
        'body': 'CSV Data Inserted Successfully!'
    }
