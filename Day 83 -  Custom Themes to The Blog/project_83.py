from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    page = ""
    return page
    
@app.route("/blog/day 76")
def hr():
  return redirect("/day 76")

@app.route("/blog/day 77")
def br():
  return redirect("/day 77")

@app.route("/day 76", methods= ["GET"])
def day_76():
    data = request.args
    template = data.get("template", "default")
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
    page = page.replace("{template}", template)

    return page

@app.route("/day 77", methods= ["GET"])
def day_77():
    data = request.args
    template = data.get("template", "default")
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
    page = page.replace("{template}", template)

    return page

app.run(host='0.0.0.0', port=5000)