#!/usr/bin/python3
import mysql.connector


def stream_users_in_batches(batch_size):
  '''
    get users from the data in batch_size
    - @batch_size: the size of the data to get
  '''
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ALX_prodev'
  )

  if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
      # Fetch the next batch of rows
      batch = cursor.fetchmany(batch_size)
      
      # If the batch is empty, we've reached the end of the data
      if not batch:
          break
      
      # Yield the batch of users
      yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
  '''
    get the batch_size users and get from them who age is over 25
    - @batch_size: the size of the batch of users
  '''
  for batch in stream_users_in_batches(batch_size):
    for user in batch:
      if user[3] > 25:
        user_data = {
            'user_id': user[0],
            'name': user[1],
            'email': user[2],
            'age': user[3]
        }
        print(user_data)
  return user_data