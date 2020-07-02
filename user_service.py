from connect_mysql import connect_mysql
import json
# Get user from db
def getUsers():
    try:
        users = []
        connection = connect_mysql()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user ",)
        for u in cursor:
            user = {}
            user["id"] = u[0]
            user["userName"] = u[1]
            users.append(user)
    except Exception as error:
        print(error.message)
    finally:
        connection.close()
        cursor.close()
    return users

# insert user to db
def addUser(user):
    try:
        connection = connect_mysql()
        cursor = connection.cursor()
        sql = "INSERT INTO USER (idUser, userName) VALUES (%s,%s)"
        cursor.execute(sql, user)
        connection.commit()
        return True
    except Exception as error:
        print(error)
        return False
    finally:
        connection.close()
        cursor.close()

# update user to db
def updateUser(user):
    try:
        connection = connect_mysql()
        cursor = connection.cursor()
        sql = "update  user set userName = {} where idUser = {}".format(user[1], user[0])
        cursor.execute(sql, user)
        connection.commit()
        return True
    except Exception as error:
        print(error)
        return False
    finally:
        connection.close()
        cursor.close()

# findUserBy id 
def findUserById(id):
    users = []
    try:
        connection = connect_mysql()
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE idUser = {}".format(id)
        cursor.execute(sql,)
        for u in cursor:
            user = {}
            user["id"] = u[0]
            user["userName"] = u[1]
            users.append(user)
    except Exception as error:
        print(error.message)
    finally:
        connection.close()
        cursor.close()
    return users

# delete user to db
def deleteUser(id):
    row = 0
    try:
        users = []
        connection = connect_mysql()
        cursor = connection.cursor()
        cursor.execute*("DELETE FROM USER WHERE idUser = {}".format(id))
        connection.commit()
        row = cursor.rowcount()
        return row
    except Exception as error:
        print(error)
        return row
    finally:
        connection.close()
        cursor.close()


if __name__ == "__main__":
  user = (8,'Thanh Hoa')
  print(deleteUser(2))
#   print(findUserById(1))
  # print(addUser(user))
#   print(getUsers())
