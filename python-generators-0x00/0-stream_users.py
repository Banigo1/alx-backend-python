#!/usr/bin/python3
import mysql.connector

def stream_users():
  '''
    get all data in the user_data table
  '''
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ALX_prodev'
  )

  if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute(
      "SELECT * FROM user_data"
    )

    for row in cursor:
      yield row
    cursor.close()
    connection.close()