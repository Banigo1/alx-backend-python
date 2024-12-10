#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
  """
    yield the users age one by one
  """
  connection = seed.connect_to_prodev()
  cursor = connection.cursor()
  cursor.execute("SELECT age FROM user_data")
  for age in cursor:
    yield age
  connection.close()
  cursor.close()


def age_average():
  sum = 0
  count = 0

  for age in stream_user_ages():
    sum += age[0]
    count += 1
  print(f'Average age of users: {float(sum) / float(count)}')


if __name__ == '__main__':
  age_average()