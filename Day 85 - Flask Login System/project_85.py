from flask import Flask, redirect, request, session, render_template
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/signup", methods=["POST"])
def createUser():
  if session.get("loggedIn"):
    return redirect("/welcome")
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route("/login", methods=["POST"])
def doLogin():
  if session.get("loggedIn"):
    return redirect("/welcome")
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"] == db[form["username"]]["password"]:
      session["loggedIn"] = form["username"]
      return redirect("/welcome")
    else:
      return redirect("/login")

@app.route("/welcome")
def welcome():
  page = f"""<h1>Hi there {db[session["loggedIn"]]["name"]}</h1>
  <button type="button" onClick="location.href='/logout'">Logout</button>
  """
  return page

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

@app.route("/login")
def login():
  if session.get("loggedIn"):
    return redirect("/welcome")
  return "template/login.html"

@app.route("/signup")
def signup():
  if session.get("loggedIn"):
    return redirect("/welcome")
  return "template/signup.html"

@app.route('/')
def index():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page = """<p><a href="/signup">Sign up</a></p>
    <p><a href="/login">Log in</a></p>"""
  return page