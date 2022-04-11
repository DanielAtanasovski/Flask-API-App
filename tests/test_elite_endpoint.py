# Created by Daniel Atanasovski - 2022

import json
from flask_app import app

# Constants
TYPE = 'application/json'
HEADERS = {
    'Content-Type': TYPE,
    'Accept': TYPE
}
MATH_ENDPOINT = '/math'


### Math Endpoints ###

def test_post_valid_integer():
    request_data = {
        'value': 20
    }

    response = app.test_client().post(
        MATH_ENDPOINT, data=json.dumps(request_data), headers=HEADERS)

    assert response.status_code == 200


def test_post_value_not_integer():
    request_data = {
        'value': 20.5
    }

    response = app.test_client().post(
        MATH_ENDPOINT, data=json.dumps(request_data), headers=HEADERS)

    assert response.status_code == 400


def test_post_response_is_max_value():
    request_data = {
        'value': 100_000_000_000
    }

    response = app.test_client().post(
        MATH_ENDPOINT, data=json.dumps(request_data), headers=HEADERS)

    assert response.get_json()['value'] == 10_000_000


def test_invalid_request_json():
    request_data = {
        'test': 'test'
    }

    response = app.test_client().post(
        MATH_ENDPOINT, data=json.dumps(request_data), headers=HEADERS)

    assert response.status_code == 400
