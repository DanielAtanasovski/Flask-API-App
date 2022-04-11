# Created by Daniel Atanasovski - 2022

from flask import Flask, Response, jsonify, request
app = Flask(__name__)  # Create App

# Constants
MATH_PAYLOAD_FIELD = 'value'
MATH_MULTIPLY_VALUE = 1337
MATH_MAX_VALUE = 10_000_000

OK_STATUS = 200
REQUEST_ERROR_STATUS = 400
UNKNOWN_ENDPOINT_ERROR_STATUS = 404
INTERNAL_ERROR_STATUS = 500


## Endpoints ##
@app.route('/', methods=['GET'])
def index_endpoint() -> Response:
    """ Return hello world to index route in JSON"""
    return jsonify(status=OK_STATUS, msg="Hello World!"), OK_STATUS


@app.route('/health', methods=['GET'])
def health_endpoint() -> Response:
    """ Return health status code in JSON"""
    return jsonify(status=OK_STATUS), OK_STATUS


@app.route('/math', methods=['POST'])
def math_endpoint() -> Response:
    """ Return a given integer multiplied by 1337 in JSON
        NOTE: The value is capped to the value defined in MATH_MAX_VALUE
    """

    endpoint_request = request.json

    if not MATH_PAYLOAD_FIELD in endpoint_request:
        return jsonify(status=REQUEST_ERROR_STATUS, msg="Field type is invalid."), REQUEST_ERROR_STATUS

    # Assume that value is formatted as such
    request_value = endpoint_request[MATH_PAYLOAD_FIELD]

    if not type(request_value) == int:
        return jsonify(status=REQUEST_ERROR_STATUS, msg="Value type is not an int."), REQUEST_ERROR_STATUS

    response_value = request_value * MATH_MULTIPLY_VALUE
    if response_value > MATH_MAX_VALUE:
        # Cap value to maximum determined by business logic
        response_value = MATH_MAX_VALUE

    return jsonify(status=OK_STATUS, value=response_value), OK_STATUS


## Error Handlers ##
@app.errorhandler(UNKNOWN_ENDPOINT_ERROR_STATUS)
def unknown_endpoint(error) -> Response:
    """ Return an error after reaching an unknown endpoint"""
    return jsonify(error=UNKNOWN_ENDPOINT_ERROR_STATUS, msg=str(error)), UNKNOWN_ENDPOINT_ERROR_STATUS


@app.errorhandler(REQUEST_ERROR_STATUS)
def bad_request_endpoint(error) -> Response:
    """ Return an error after recieving a bad request"""
    return jsonify(error=REQUEST_ERROR_STATUS, msg=str(error)), REQUEST_ERROR_STATUS


@app.errorhandler(INTERNAL_ERROR_STATUS)
def internal_error_endpoint(error) -> Response:
    """ Return an error after internal error occurred"""
    return jsonify(error=INTERNAL_ERROR_STATUS, msg=str(error)), INTERNAL_ERROR_STATUS


if __name__ == "__main__":
    app.run(host="0.0.0.0")
