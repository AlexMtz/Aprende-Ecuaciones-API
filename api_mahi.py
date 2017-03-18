# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask
from dbhelper import DBHelper
import json
from flask import request
import os
app = Flask (__name__)

@app.route("/api/v1/")
def index():
    return "Welcome to the API!"

@app.route("/api/v1/user")
def user():
    DB = DBHelper()
    username = request.args.get("u")
    if username is not None:
    	json_data = {}
        user = DB.get_user(username)
        if user is not None:
        	json_data['username'] = user[2]
        	json_data['email'] = user[1]
        else:
        	json_data['username'] = 'No exists'
        	json_data['email'] = 'not_exists@email.com'
    else:
    	json_data = []
        users = DB.get_all_users()
        if users is not None:
            for u in users:
                user_data = {}
                user_data['username'] = u[2]
                user_data['email'] = u[1]
                json_data.append(user_data)
    return json.dumps(json_data)

@app.route("/api/v1/user/verify", methods=['POST'])
def verify_user():
    DB = DBHelper()
    username_to_verify = request.get_json(force=True)
    user = DB.get_user(username_to_verify['username'])
    result = {}
    if user is not None:
    	if username_to_verify['password'] == user[3]:
    		result['status'] = 1
    		result['message'] = username_to_verify['username'] + ' is a valid user'
    	else:
    		result['status'] = 2
    		result['message'] = username_to_verify['username'] + ' is a not valid user'
    else:
    	result['status'] = 0
    	result['message'] = username_to_verify['username'] + ' is not register in the Mahi system'
    return json.dumps(result)

@app.route("/api/v1/user/registry", methods=['POST'])
def insert_user():
    DB = DBHelper()
    username_to_registry = request.get_json(force=True)
    result = {}
    if username_to_registry is not None:
    	if username_to_registry['email'] is not None and username_to_registry['username'] is not None and username_to_registry['password'] is not None:
    		try:
    			DB.insert_user(username_to_registry['email'],username_to_registry['username'],username_to_registry['password'])
    			result['status'] = 1
    			result['message'] = username_to_registry['username'] + ' registred successful'
    		except Exception as e:
    			result['status'] = 3
    			result['message'] = username_to_registry['username'] + ' can\'t be registred because it already exists'
    	else:
    		result['status'] = 2
    		result['message'] = username_to_registry['username'] + ' registred failed, all information is required'
    else:
    	result['status'] = 0
    	result['message'] = ' Please send an information about the user'
    return json.dumps(result)

@app.route("/api/v1/user/update", methods=['POST'])
def update_user():
    DB = DBHelper()
    username_to_registry = request.get_json(force=True)
    result = {}
    if username_to_registry is not None:
    	if username_to_registry['email'] is not None and username_to_registry['username'] is not None and username_to_registry['password'] is not None:
    		try:
    			DB.update_user(username_to_registry['email'],username_to_registry['username'],username_to_registry['password'])
    			result['status'] = 1
    			result['message'] = username_to_registry['username'] + ' updated successful'
    		except Exception as e:
    			result['status'] = 3
    			result['message'] = username_to_registry['username'] + ' can\'t be updated because some was wrong'
    	else:
    		result['status'] = 2
    		result['message'] = username_to_registry['username'] + ' update failed, all information is required'
    else:
    	result['status'] = 0
    	result['message'] = ' Please send an information about the user'
    return json.dumps(result)

@app.route("/api/v1/user/score")
def score_user():
    return "Welcome to the API!!!"

@app.route("/api/v1/attempt/registry", methods=['POST'])
def attemp_user():
    DB = DBHelper()
    attempt_to_registry = request.get_json(force=True)
    print attempt_to_registry['calificacion']
    result = {}
    if attempt_to_registry is not None:
    	if attempt_to_registry['usuario'] is not None:
    		try:
    			DB.registry_attempt(attempt_to_registry['usuario'],attempt_to_registry['genero'],attempt_to_registry['edad'],attempt_to_registry['ecuacion'],attempt_to_registry['dificultad'],attempt_to_registry['tiempo'],attempt_to_registry['calificacion'],attempt_to_registry['fecha'])
    			result['status'] = 1
    			result['message'] = attempt_to_registry['usuario'] + ' registred successful'
    		except Exception as e:
    			result['status'] = 3
    			result['message'] = attempt_to_registry['usuario'] + ' can\'t be registred :('
    			print e
    	else:
    		result['status'] = 2
    		result['message'] = attempt_to_registry['usuario'] + ' registred failed, all information is required'
    else:
    	result['status'] = 0
    	result['message'] = ' Please send an information about the attempt'
    return json.dumps(result)

@app.route("/api/v1/attempt", methods=['GET'])
def attemp():
    DB = DBHelper()
    json_data = []
    attempts = DB.get_all_attempt()
    if attempts is not None:
        for a in attempts:
            attempt_data = {}
            attempt_data['usuario'] = a[1]
            attempt_data['genero'] = a[2]
            attempt_data['edad'] = a[3]
            attempt_data['ecuacion'] = a[4]
            attempt_data['dificultad'] = a[5]
            attempt_data['tiempo'] = a[6]
            attempt_data['calificacion'] = a[7]
            attempt_data['fecha'] = a[8]
            json_data.append(attempt_data)
    return json.dumps(json_data)

@app.route("/api/v1/workbooks")
def workbooks_user():
    return "Welcome to the API!!!"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)