import os

from fastapi import APIRouter

from settings import CLOUDFRONT_URL
from consts import JSON_URL, MIN_PRICE, S3_BUCKET_NAME, OUTPUT_FILE_NAME
from backend.data_process import get_json_data, filter_json_data, save_json_to_file, verify_json
from backend.aws_operations import upload_to_s3, download_from_cloudfront

router = APIRouter()


@router.get("/products")
def process_json_data() -> dict:
    """
    Process and upload product data to S3.
    This route retrieves product data from a specified source, filters the
    data based on a minimum price, saves it to a file, and then uploads this file
    to an S3 bucket. It returns a success status if all operations are successful.
    :return: dict: indication with status success or error
    """
    try:
        raw_products = get_json_data(JSON_URL)
        filtered_products = filter_json_data(raw_products, MIN_PRICE)
        save_json_to_file(filtered_products, OUTPUT_FILE_NAME)
        upload_to_s3(S3_BUCKET_NAME, OUTPUT_FILE_NAME)
        return {"status": "success"}
    except Exception as e:
        return {"status": f"error", "message": str(e)}


@router.get("/verify")
def verify():
    """
    Verifies the accessibility and format of product data via CloudFront.
    This route downloads the product data file from a CloudFront URL and checks
    if it is in a valid JSON format. It returns a success status with a validation
    message if the data is accessible and valid.
    :return: dict: indication with status success or error, also a message with additional info.
    """
    try:
        cloudfront_endpoint = CLOUDFRONT_URL + '/' + OUTPUT_FILE_NAME
        json_file = download_from_cloudfront(cloudfront_endpoint)
        is_valid_json = verify_json(json_file)
        return {"status": "success" if is_valid_json else "error",
                "is_valid_json": is_valid_json}
    except Exception as e:
        return {"status": "error", "message": str(e)}
