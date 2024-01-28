import requests
import json


def get_json_data(url) -> list[dict]:
    """
    Retrieves JSON data from a given URL and extracts a list of products.

    :param url: URL to fetch the JSON data from.
    :raise: HTTPError: when the request fail.
    :return: ist of dictionaries, where each dictionary is a product.
    """
    response = requests.get(url)
    response.raise_for_status()
    products = response.json().get('products', [])
    return products


def filter_json_data(products: list[dict], min_price: int) -> list[dict]:
    """
    Filters a list of product dictionaries based on a minimum price.

    :param products: list of product dictionaries to be filtered.
    :param min_price: minimum price threshold
    :return:The filtered list of product dictionaries.
    """
    return [product for product in products if product.get('price', 0) >= min_price]


def save_json_to_file(products: list[dict], file_name: str) -> None:
    """
    Saves a list of products to a file in JSON format.

    :param products: list of product dictionaries to be filtered.
    :param file_name: name of the file where the JSON data will be stored.
    :return: None
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)


def verify_json(data) -> bool:
    """
    Validates whether the provided data is in valid JSON format.
    :param data: data to then validate if json.
    :return: indication weather data is json or not.
    """
    if isinstance(data, (dict, list)):  # checks if data valid json type (list or dict)
        return True
    try:
        parsed_json = json.loads(data)
        if isinstance(parsed_json, (dict, list)):
            return True
    except (TypeError, json.JSONDecodeError):
        return False
