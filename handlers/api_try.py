import random
import requests
import json


def get_pet_by_id(pet_id):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, headers)
    return response


def update_pet(pet_id, name, status):
    url = f"https://petstore.swagger.io/v2/pet/"
    payload = json.dumps({
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": "fish"
        },
        "name": name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 34567892,
                "name": name
            }
        ],
        "status": status
    })
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


def create_new_pet():
    url = "https://petstore.swagger.io/v2/pet"
    random_id = random.randrange(10000, 30000)
    payload = json.dumps({
        "id": random_id,
        "category": {
            "id": random_id,
            "name": "fish"
        },
        "name": "goldy",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 34567892,
                "name": "goldy"
            }
        ],
        "status": "available"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response