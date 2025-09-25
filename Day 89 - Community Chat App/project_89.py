from flask import Flask, request, redirect
import datetime
from replit import db

app = Flask(__name__)

def get_chat(user):
  message = ""
  userid = request.headers['X-Replit-User-Id']
  print(userid)
  f = open("temporary/message.html", "r")
  message = f.read()
  f.close()
  keys = db.keys()
  keys = list(keys)
  result = ""
  recent = 0
  for key in reversed(keys):
    my_message = message
    my_message = my_message.replace("{username}", db[key]["username"])
    my_message = my_message.replace("{timestamp}", key)
    my_message = my_message.replace("{message}", db[key]["message"])
    if userid  == "27422703":
      my_message = my_message.replace("{admin}", "")
    else:
      my_message = my_message.replace("{admin}", f"""<a href="/delete?id={key}"> ❌</a>""")
    result += my_message
    recent += 1
    if recent == 5:
      break
  return result

@app.route('/')
def index():
  page = ""
  f = open("temporary/chat.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{username}", request.headers["X-Replit-User-Name"])
  page = page.replace( "{chats}", get_chat(request.headers[ "X-Replit-User-Id"]))
  return page 

@app.route('/add', methods=["POST"]) 
def add():
  form = request.form
  message = form["message"]
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  userid = request.headers["X-Replit-User-Id"]
  username = request.headers["X-Replit-User-Name"]
  db[timestamp] = {"userid": userid, "username": username, "message": message}
  return redirect("/")

@app.route('/delete', methods=["GET"])
def delete():
  if request.headers["x-replit-user-Name"] == "guruharish128":
    return redirect("/")
  results = request.values["id"]
  del db[results]
  return redirect("/")