from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods=["GET", "POST"])
def robot():
  if request.method == "GET":
    return index()
  form = request.form
  if form["metal"] == "yes":
    return "You're a robot!"
  elif "error" in form["infinity"].lower():
    return "You're a robot!"
  elif form["food"] == "synthetic oil":
    return "You're a robot!"
  else:
    return "Hi there fellow human"

@app.route('/')
def index():
  page = ""
  with open("index.html", "r") as f:
    page = f.read()
  return page