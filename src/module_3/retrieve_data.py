import boto3
import os
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()

# AWS credentials
aws_access_key_id = os.environ['aws_access_key_user']
aws_secret_access_key = os.environ['aws_secret_key']

# Initialize a session with boto3
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
# Create an S3 client
s3 = session.client('s3')

# Define the S3 bucket and object you want to download
s3_bucket = 'zrive-ds-data'
s3_object_key = 'groceries/box_builder_dataset/feature_frame.csv'

# Define a local directory and file path to save the downloaded file
local_directory = '/Users/alvarochapela/Documents/DATOS_ZRIVE/Module2Data'
local_file_name = 'feature_frame.csv'
local_file_path = os.path.join(local_directory, local_file_name)

# Create the local directory if it doesn't exist
os.makedirs(local_directory, exist_ok=True)

# Download the file from S3 to the local directory
s3.download_file(s3_bucket, s3_object_key, local_file_path)

print(f"Downloaded {s3_object_key} from S3 bucket {s3_bucket} to {local_file_path}")