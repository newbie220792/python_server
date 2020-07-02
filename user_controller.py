from flask import Flask, request
from flask import jsonify
import json
from user_service import *
app = Flask(__name__)

result = json.loads('{"status": "", "error":"null", "data":"" }')


@app.route('/users', methods=['GET'])
def fechtUsersController():
    try:
      users = getUsers()
      if len(users) > 0:
        result["status"] = "success"
        result["data"] = users
      else:
        result["status"] = "falied"
        result["error"] = "The users is empty"
    except Exception as error:
      result["status"] = "falied"
      result["error"] = error.message
    return json.dumps(result)


@app.route('/user/<int:id>', methods=['GET'])
# get User by ID
def findUserController(id):
   try:
      users = findUserById(id)
      if len(users) > 0:
        result["status"] = "success"
        result["data"] = users
      else:
        result["status"] = "falied"
        result["error"] = "Can not get user"
   except Exception as error:
      result["status"] = "falied"
      result["error"] = error.message
   return  json.dumps(result)


@app.route('/addUser' , methods = ['POST'])
def addUserController(user):
    return addUser(user)


@app.route('/delete/user/<int:id>' , methods = ['GET'])
def deleteUserController(id):
   try:
      if deleteUser(id):
        result["status"] = "success"
      else:
        result["status"] = "falied"
        result["error"] = "Delete user by id = {} fail".format(id)
   except Exception as error:
      result["status"] = "falied"
      result["error"] = error.message
   return  json.dumps(result)



@app.route('/users' , methods = ['POST'])
def updateUserController(user):
    return updateUser(user)

@app.errorhandler(404)
def notFoundController(error = None):
  result["status"] = "404"
  result["error"] = "Not found" + request.url,
  resp = jsonify(result)
  resp.status_code = 404
  return resp


if __name__ == '__main__':
    app.run(debug=True)
