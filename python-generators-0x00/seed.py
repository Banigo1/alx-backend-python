#!/usr/bin/python3
import mysql.connector
import csv
import uuid

# connect to the databas
def connect_db():
  """
    Connects to the MySQL database server.
    Returns the connection object if successful, None otherwise.
  """
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
  )

  if connection.is_connected():
    return connection
  return None

# create the database
def create_database(connection):
  """
    Creates the database ALX_prodev if it does not exist.
  """
  cursor = connection.cursor()
  cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
  connection.commit()
  cursor.close()

# connect to the database
def connect_to_prodev():
  """
    Connects to the ALX_prodev database in MySQL.
    Returns the connection object if successful, None otherwise.
  """
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ALX_prodev'
  )
  if connection.is_connected():
    return connection
  return None

# create table in database
def create_table(connection):
  '''
    crete table if not exists  user_data
      user_id(Primary Key, UUID, Indexed)
      name (VARCHAR, NOT NULL)
      email (VARCHAR, NOT NULL)
      age (DECIMAL,NOT NULL)
  '''
  cursor = connection.cursor()
  cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(10) NOT NULL
        )
    ''')
  connection.commit()
  cursor.close()
  
def insert_data(connection, data):
  '''
    insert data in the database using csv file
    @connection: the connection of the database
    @data: the csv file
  '''
  with open(data, 'r') as f:
    # read the file
    reader = csv.reader(f)

    # skip the header
    next(reader)

    # define the cursor of the database
    cursor = connection.cursor()

    # read each line
    for row in reader:
      name = row[0]
      email = row[1]
      age = int(row[2])
      user_id = str(uuid.uuid4())
      cursor.execute(
        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
        (user_id, name, email, age)
      )
    connection.commit()
    cursor.close()