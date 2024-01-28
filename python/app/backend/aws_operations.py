import boto3
import os
import requests


def upload_to_s3(bucket_name, file_name):
    """
    uploads a file specified by `file_name` to the S3 bucket
    named `bucket_name` using the AWS SDK for Python (Boto3).
    :param bucket_name: S3 bucket where the file will be uploaded
    :param file_name: name of the file to upload
    :return: None
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    with open(file_name, 'rb') as data:
        s3.upload_fileobj(data, bucket_name, file_name)


def download_from_cloudfront(cloudfront_url: str) -> dict:
    """
    Downloads JSON data from a given CloudFront URL.
    If the response status code is not successful (200), an HTTPError is raised.
    :param: cloudfront_url: CloudFront URL to download file from s3
    :raise: HTTPError: If the HTTP request returned an unsuccessful status code.
    :return: Dictionary with the json response
    """
    response = requests.get(cloudfront_url)
    response.raise_for_status()  # will raise HTTPError in case status code is not success
    return response.json()
