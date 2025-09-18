from flask import Flask, request

app = Flask(__name__)

users = {}
users["marta"] = {"email": "m@m.com", "password": "admin1"}
users["john"] = {"email": "b@b.com", "password": "admin2"}
users["jane"] = {"email": "c@c.com", "password": "admin3"}

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return index()
  
  form = request.form
  details = {}
  try:
    details = users[form["username"]]
  except KeyError:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email or password incorrect"

@app.route('/')
def index():
  page = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Login form</title>
</head>
<body>
  <h1>Login form</h1>
  <form method = "post" action = "/login">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Password: <input type="password" name="password"> </p>
    <button type="submit">Login</button>
  </form>
</body>
</html>
    """
  return page