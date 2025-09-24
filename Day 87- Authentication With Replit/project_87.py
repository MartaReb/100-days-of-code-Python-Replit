from flask import Flask, redirect, request, session
from replit import db
import os

replit_username = "marta"

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.urandom(24)

db["user"] = {"username": "marta", "password": "admin123"}

def get_blogs():
  entry = ""
  with open("template/entry.html", "r") as f:
    entry = f.read()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    this_entry = entry
    if key != "user":
      this_entry = this_entry.replace("{title}", db[key]["title"])
      this_entry = this_entry.replace("{date}", db[key]["date"])
      this_entry = this_entry.replace("{body}", db[key]["body"])
      content += this_entry
  return content

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Name']
  if userid == replit_username:
    return redirect("/edit")
  page = ""
  with open("template/blog.html", "r") as f:
    page = f.read()
  page = page.replace("{content}", get_blogs())
  return page

@app.route('/loginForm')
def loginForm():
  userid = request.headers['X-Replit-User-Name']
  if userid == replit_username:
    return redirect("/edit")
  page = ""
  with open("tempalte/login.html", "r") as f:
    page = f.read()
  return page

@app.route('/login', methods=["POST"])
def login():
  userid = request.headers['X-Replit-User-Name']
  if userid == replit_username:
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] and form["password"] == db[
      "user"]["password"]:
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route("/edit")
def edit():
  userid = request.headers['X-Replit-User-Name']
  print(userid)
  if userid != replit_username:
    return redirect("/")
  page = ""
  with open("tempalte/edit.html", "r") as f:
    page = f.read()
  page = page.replace("{content}", get_blogs())
  return page

@app.route("/add", methods=["POST"])
def add():
  userid = request.headers['X-Replit-User-Name']
  if userid != replit_username:
    return redirect("/")
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")