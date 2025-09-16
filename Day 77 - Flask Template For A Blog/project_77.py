from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    page = ""
    return page
@app.route("/blog/day 76")
def hr():
  return redirect("/day 76")

@app.route("/blog/day 77")
def br():
  return redirect("/day 77")

@app.route('/hello/day 76')
def hello():
    title = "Day 76 on my programming journey"
    date = "September 15th"
    text = "Here is my coding project from 76 day."
    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)

    return page

@app.route('/day 77')
def bye():
    title = "Day 77 on my programming journey"
    date = "September 16th"
    text = "Here is my coding project from 76 day."
    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)

    return page