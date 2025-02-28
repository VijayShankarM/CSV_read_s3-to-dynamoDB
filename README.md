# S3 to DynamoDB CSV Processor

## Overview
This project sets up an AWS pipeline that automatically processes CSV files uploaded to an S3 bucket and inserts the data into DynamoDB using AWS Lambda.

## Step 1: Setup AWS Services
- **S3** → Stores the CSV files
- **AWS Lambda** → Processes the CSV and inserts data into DynamoDB
- **DynamoDB** → Stores structured data

## Step 2: Create an S3 Bucket
1. Go to **AWS S3 Console** → Click **Create Bucket**
2. Enter a unique **Bucket Name** (e.g., `csv-upload-bucket`)
3. **Block Public Access** → Keep all options enabled (for security)
4. Click **Create bucket**

## Step 3: Create a DynamoDB Table
1. Go to **AWS DynamoDB Console** → Click **Create Table**
2. Enter the following details:
   - **Table Name**: `CSVData`
   - **Partition Key**: `id` (String) – Unique identifier for each row
3. Click **Create table**

## Step 4: Create an AWS Lambda Function
1. Go to **AWS Lambda Console** → Click **Create function**
2. Select **Author from scratch**
3. Enter:
   - **Function Name**: `CSVProcessor`
   - **Runtime**: Python 3.x
   - **Permissions**: Attach an IAM Role with access to S3 and DynamoDB
4. Click **Create function**

## Step 5: Attach an S3 Trigger to Lambda
1. Open **CSVProcessor** function → Go to **Triggers**
2. Click **Add trigger**
3. Select **S3**
4. Choose the **S3 bucket** created earlier
5. Set **Event type**: `PUT` (Object Created)
6. Click **Add**

## Step 6: Write and Deploy the Lambda Function
1. Open **CSVProcessor** → Go to **Code**
2. Replace existing code with the Python script that:
   - Reads the CSV file from S3
   - Parses the CSV contents
   - Inserts each row into DynamoDB
3. Click **Deploy**

## Step 7: Upload a CSV File to S3
1. Go to **AWS S3 Console** → Open `csv-upload-bucket`
2. Click **Upload** → Choose a sample CSV file
3. Click **Upload**
4. Lambda will automatically process the file and store data in DynamoDB

## Step 8: Verify Data in DynamoDB
1. Go to **AWS DynamoDB Console**
2. Open the `CSVData` table
3. Click **Explore Table Items**
4. Check if the data is inserted correctly

✅ **The pipeline is now fully functional!** 🎉

