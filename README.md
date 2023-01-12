# Simple Python Flask Endpoint

A simple flask app that contains a few endpoints that respond to GET and POST requests.

### Requirements

The requirements of the challenge are listed below:

##### Application Details
Your application should be a simple, small, operable web-style API. It should implement the following:
Using Python Flask create two simple endpoints as described below
1.	A health endpoint which returns an appropriate response code i.e. 200 response showing application is up
2.	A simple elite 'math' endpoint using multiplication to multiply the posted number (in JSON payload) by 1337 and return the result in JSON
    1.	Max limit on returned value is 10,000,000
    2.	200 response code is returned for successful processing and return
    3.	Non-200 response code is returned for unsuccessful processing
3.	A test suite using PyTest
    1.	Test proving posted value not an integer will return a 400 response i.e. double, float or alpha
    2.	Test proving returned number generated is not greater than 10,000,000 returning a 400 response
    3.	Test invalid JSON posted in returns a 400

##### Fit and Finish
Once the application has been written, continue with the following additions:
1.	Provide a means of packaging your application as a Dockerfile build
2.	Write a clear and understandable README which explains your application, its architecture, packaging steps, how to run it, and how it aligns with the listed requirements
 
#### Architecture 

The application satisfies the requirements of the challenge where the '/health' and '/math' endpoints are implemented and are responding to the relevant requests. 

All the logic is located within the 'flask_app.py' file, implementing functions to handle the responses to the relevant endpoints, as well as responses to errors such as 400, 404 and 500. Constants are outlined at the top of the file for quick adjustments to the field name of the payload to expect on the '/math' endpoint, the value to multiple said field and as well as the maximum value to respond with. 

Test cases were also implemented to cover the business logic outlined in the requirements regarding the '/math' endpoint.

*It is assumed that a number posted to the '/math' endpoint and resulting in a response capped to the defined maximum value (10,000,000) would not be invalid and as such still returning a 200 OK status.*

### Endpoints

**'/'** - Responds to GET requests with Hello World!.

**'/health'** - Responds to GET requests with the status code of the service.

**'/math'** - Responds to POST requests containing a 'value' field in integer format with the value multiplied by 1337.

### Dependencies

Dependencies are listed below, and in the requirements.txt provided.
```
Python3
pytest
flask
```
*Tested on python 3.9*
### Installation / Running

#### Python
Can be run directly with:
`python ./flask_app.py`

#### Docker
Build the docker image:
`docker build -t flask-app:latest .`

Run the docker image:
`docker run -d -p 5000:5000`

The result should be an API service accessible from 'localhost:5000' or '127.0.0.1:5000' of which GET and POST requests can be sent.

### Examples
The API contains a GET endpoint of health, which responds to the '/health' endpoint with the status of the service.

JSON post requests can be made to the '/math' endpoint, for example sending the following JSON structure in post request:
`{ "value" : 20 }`
would be responded to with the following JSON response:
`{ "status": 200, "value" : 26740 }`

### Testing

The project contains a few test cases which can be run in the source directory with the following command:
`pytest`
