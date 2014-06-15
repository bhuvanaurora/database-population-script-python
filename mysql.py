#!/usr/bin/python

import MySQLdb
import readfile

#Open database connection
db = MySQLdb.connect("localhost", "bhuvan", "pass@1234", "gruppidb")

#Prepare a curson object using cursor() method
cursor = db.cursor()

names = readfile.main()

for name in names[0]:
  sql =  """INSERT INTO users(username,
  	   password, email, role)
	   VALUES ('""" + name + """', '""" + name + """', '""" +  name + """@gmail.com', 'admin')"""
  cursor.execute(sql)
  db.commit()
db.close() 
