# CSV_read_s3-to-dynamoDB
This project automates the process of uploading a CSV file to Amazon S3, processing it using AWS Lambda, and storing the extracted data into Amazon DynamoDB. The entire workflow is event-driven, meaning when a CSV file is uploaded to S3, Lambda automatically processes it and inserts the data into DynamoDB.
