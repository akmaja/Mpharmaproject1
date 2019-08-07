# codeapp

STEPS TO BUILD EST API

1. Setup database environment
install postgresl

2. Install the following module
a. flask
b. flask-sqlalchemy
c. flask-marshmallow
d. marshmallow-sqlalchemy
e. OS


3. Create a working folder called "code_api"

4. Create a file called myapp.py and add attached source codes

5. To test API, download and install postman from https://www.getpostman.com/downloads/. Sign up with gmail account

6. To Add POST new code, use the following steps
a. Type http://127.0.0.1:5000/code in Postman
b. Select content-type and application/json for the headers
c. use the json data below for testing
{
	"category_code" : "A35",
	"diagnosis_code" : 30,
	"full_code": "A030",
	"abv_description" : "delete, unspecified",
	"full_description" : "Typhoid, unspecified",
	"category_title" : "Typhoid"
	
}

d. Click Send

7. To GET all codes
a. Select GET in postman and enter http://127.0.0.1:5000/code
b. Click Send button

8. Get single code
a. Select GET in postman and enter http://127.0.0.1:5000/code/id where id is key for row (eg.  http://127.0.0.1:5000/code/2)

9.To update a code use PUT method
a. Type http://127.0.0.1:5000/code/id in Postman where id is the full_code of the row
b. Select content-type and application/json for the headers
c. use the json data below for testing
{
	"category_code" : "A35",
	"diagnosis_code" : 30,
	"full_code": "A030",
	"abv_description" : "delete, unspecified",
	"full_description" : "Typhoid, unspecified",
	"category_title" : "Typhoid"
	
}

d. Click Send

10. Delete a code
a. Select DELETE in postman and enter http://127.0.0.1:5000/code/id where id is key for row (eg.  http://127.0.0.1:5000/code/2)