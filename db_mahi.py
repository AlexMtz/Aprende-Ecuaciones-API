import pymysql
import db_config

connection = pymysql.connect(host='localhost',
	user = db_config.db_user,
	passwd = db_config.db_password)
try:
	with connection.cursor() as cursor:
		sql = "CREATE DATABASE IF NOT EXISTS equationsdb"
		cursor.execute(sql)
		sql = "CREATE TABLE IF NOT EXISTS equationsdb.attempt (ID int NOT NULL AUTO_INCREMENT, USERNAME VARCHAR(30) NOT NULL, GENRE VARCHAR(10) NOT NULL, AGE INT NOT NULL, EQUATION VARCHAR(50) NOT NULL, DIFICULTY VARCHAR(5) NOT NULL, TIME INT NOT NULL, SCORE FLOAT NOT NULL, DATE VARCHAR(10) NOT NULL, PRIMARY KEY(id));"
		cursor.execute(sql)
		connection.commit()
finally:
	connection.close()
