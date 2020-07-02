#!/usr/bin/python
import mysql.connector as mariadb
# from mysql import mysql.connector
def connect_mysql():
  try:
    con = mariadb.connect(user='root',
      password='',
      database='home',
      host='localhost')
  except mariadb.Error as error:
    print('Error: {}'.format(error.message))
  return con

# if __name__ == '__main__':
#   print(connect_mysql())