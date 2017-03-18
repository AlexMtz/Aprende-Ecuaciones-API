# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: dbhelper.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Esun archivo auxiliar que permite realizar la conexión a la base de datos donde se almacenan
#   los reviews de la pagina 'https://www.rottentomatoes.com/'.
#
#                                           dbhelper.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Conectar con la DB   | - Cuenta con un método |
#           |     DataManager       |    que contiene los     |   que realiza la       |
#           |                       |    reviews de la página |   conexión a la DB.    |
#           |                       |    Rotten Tomatoes.     | - Ceunta con un método |
#           |                       |                         |   que consulta todos   |
#           |                       |                         |   los reviews almacena-|
#           |                       |                         |   dos en la DB.        |
#           +-----------------------+-------------------------+------------------------+
#
#	Instrucciones de ejecución:
#		- Este archivo no se ejecuta, se utiliza dentro del microservicio de reviews_mc.py
#
#
import pymysql
import db_config
import datetime

class DBHelper:
	def connect(self, database="equationsdb"):
		return pymysql.connect(host='localhost',
			user = db_config.db_user,
			passwd = db_config.db_password,
			db = database)

	def get_all_users(self):
		connection = self.connect()
		try:
			query = "SELECT * FROM equationsdb.user;"
			with connection.cursor() as cursor:
				cursor.execute(query)
			return cursor.fetchall()
		finally:
			connection.close()

	def get_user(self, username):
		connection = self.connect()
		try:

			query = "SELECT * FROM equationsdb.user WHERE USERNAME = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query,username)
			return cursor.fetchone()
		finally:
			connection.close()

	def insert_user(self, email, username, password):
		connection = self.connect()
		try:

			query = "INSERT INTO equationsdb.user (EMAIL, USERNAME, PASSWORD) VALUES ('"+email+"','"+username+"',%s);"
			with connection.cursor() as cursor:
				cursor.execute(query,password)
				connection.commit()
		finally:
			connection.close()

	def update_user(self, email, username, password):
		connection = self.connect()
		try:

			query = "UPDATE equationsdb.user SET PASSWORD = %s WHERE USERNAME = '" + username +"';"
			with connection.cursor() as cursor:
				cursor.execute(query,password)
				connection.commit()
		finally:
			connection.close()

	def registry_attempt(self, username, genre, age, equation, dificulty, time, score, date):
		connection = self.connect()
		try:
			query = "INSERT INTO equationsdb.attempt (USERNAME, GENRE, AGE, EQUATION, DIFICULTY, TIME, SCORE, DATE) VALUES ('"+username+"','"+genre+"',"+str(age)+",'"+equation+"','"+dificulty+"',"+str(time)+","+str(score)+",'"+date+"');"
			print query
			with connection.cursor() as cursor:
				cursor.execute(query)
				connection.commit()
		finally:
			connection.close()

	def get_all_attempt(self):
		connection = self.connect()
		try:
			query = "SELECT * FROM equationsdb.attempt;"
			with connection.cursor() as cursor:
				cursor.execute(query)
			return cursor.fetchall()
		finally:
			connection.close()