# aws-s3-python

# file_upload.py

## This function uploads a file to an S3 bucket
## The upload file function expects 3 arguments:
### file_name - The name of the EXISTING file that you would like uploaded, the script will look for this file in the same directory that the script is stored.
### bucket - The name of the bucket that you would like the file uplaoded to.
### object_name - A string specifying what you would like the file to be named when it is stored in the S3 bucket.
## This function returns a string notifying wether of wether or not the file was uploaded successfully