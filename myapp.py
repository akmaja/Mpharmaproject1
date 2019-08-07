#install the following modules (flask,flask-sqlalchemy, flask-marshmallow, marshmallow-sqlalchemy)
#flask ===> web framework built with a small core 
#flask-SQLAlchemy ===> an extension for Flask that adds support for SQLAlchemy to your application
#flask-marshmallow ===> an object serialization/deserialization library
#OS  ===> The OS module in python provides functions for interacting with the operating system. It will be used to set base url for our database

#import modules
import sqlalchemy
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine


#init app
app = Flask(__name__)

#Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:penguin7@localhost:5432/Practice Test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#initialize SQLAlchemy
db = SQLAlchemy(app)

#initialize Marshmallow
ma = Marshmallow(app)

#code Class/Model
class codestxt_file(db.Model):

	#create fields
	category_code = db.Column(db.String(200))
	diagnosis_code = db.Column(db.String(200))
	full_code = db.Column(db.String(200), primary_key=True)
	abv_description = db.Column(db.String(200))
	full_description = db.Column(db.String(200))
	category_title = db.Column(db.String(200))

	#initialise or constructor
	def __init__(self, category_code, diagnosis_code, full_code, abv_description, full_description, category_title):
		self.category_code = category_code
		self.diagnosis_code = diagnosis_code
		self.full_code = full_code
		self.abv_description = abv_description
		self.full_description = full_description
		self.category_title = category_title

#create code schema
class CodeSchema(ma.Schema):
	#indicate fields you want to show
	class Meta:
		fields = ('category_code', 'diagnosis_code', 'full_code', 'abv_description', 'full_description', 'category_title')

#initialize schema
#for single row
code_schema = CodeSchema(strict=True)
#for many rows
codes_schema = CodeSchema(many=True, strict=True) 


#create a code
#create a route and restrict it to POST method
@app.route('/code', methods=['POST'])
def add_code():
	category_code = request.json['category_code']
	diagnosis_code = request.json['diagnosis_code']
	full_code = request.json['full_code']
	abv_description = request.json['abv_description']
	full_description = request.json['full_description']
	category_title = request.json['category_title']

	#receive new entry
	new_code = codestxt_file(category_code, diagnosis_code, full_code, abv_description, full_description, category_title)

	#store data into table
	db.session.add(new_code)
	db.session.commit()

	return code_schema.jsonify(new_code)

#get all codes
@app.route('/code', methods=['GET'])
def get_codes():
	all_codes = codestxt_file.query.all()
	result = codes_schema.dump(all_codes)
	return jsonify(result.data)

#get single code
@app.route('/code/<id>', methods=['GET'])
def get_code(id):
	code = codestxt_file.query.get(id)
	result = code_schema.dump(code)
	return jsonify(result.data)

#update a code
@app.route('/code/<full_code>', methods=['PUT'])
def update_code(full_code):
	fetch_codes = codestxt_file.query.get(full_code)

	category_code = request.json['category_code']
	diagnosis_code = request.json['diagnosis_code']
	full_code = request.json['full_code']
	abv_description = request.json['abv_description']
	full_description = request.json['full_description']
	category_title = request.json['category_title']

	fetch_codes.category_code = category_code
	fetch_codes.diagnosis_code = diagnosis_code
	fetch_codes.full_code = full_code
	fetch_codes.abv_description = abv_description
	fetch_codes.full_description = full_description
	fetch_codes.category_title = category_title

	db.session.commit()

	return code_schema.jsonify(fetch_codes)


#delete code
@app.route('/code/<full_code>', methods=['DELETE'])
def delete_code(full_code):
	code = codestxt_file.query.get(full_code)
	db.session.delete(code)
	db.session.commit()

	result = code_schema.dump(code)
	return jsonify(result.data)


#Fetch codes in batches of 20
@app.route('/code/page/<int:page_num>', methods=['GET'])
def get_codes_batches(page_num):
	codes =codestxt_file.query.paginate(per_page=20, page=page_num, error_out=True)
	#result = codes_schema.dump(codes)
	#return jsonify(result.data)
	return render_template('index.html', threads=codes)

# Run Server
if __name__ == '__main__':
	app.run(debug=True)