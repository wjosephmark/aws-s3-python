import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
  s3_client = boto3.client('s3')

  if object_name is None:
    object_name = os.path.basename(file_name)

  try:
    response = s3_client.upload_file(file_name, bucket, object_name)
  except ClientError as e:
    print(e)
    return 'Failed to upload file'
  return 'File uploaded successfully'

response = upload_file('file_name.txt', 'wjm-test-bucket')

print(response)