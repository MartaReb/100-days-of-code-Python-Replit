from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = """
  <html>
  <body>
    <h1>Welcome!<h1>
    <p>Go on my <a href = "/portfolio">portfolio</a> page or <a href = "/linktree">linktree</a> page</p>
  </body>
  </html>
  """

  return page

@app.route('/portfolio') 
def portfolio():
  page = """<!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My portfolio</title>
    <link href="static/portfolio_style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Marta's Portfolio</h1>
    <p>Solutions for 2 challenges from Replit's "100 Days of Code - The Complete Python Course"</p>
    <h2>Day 66 - GUI calculator</h2>
    <p>My project is a simple GUI calculator.</p>
    <a href = "https://github.com/MartaReb/100-days-of-code-Python-Replit/blob/main/Day%2066%20-%20GUI%20calculator/project_66.py"><img src="static/images/day_66.jpg" width = 30%></a>
    <h2>Day 72 - Secure Private Diary</h2>
    <p>A diary program with a protection.</p>
    <a href = "https://github.com/MartaReb/100-days-of-code-Python-Replit/blob/main/Day%2072%20-%20Secure%20Private%20Diary/project_72.py"><img src="static/images/day_72.jpg" width = 30%></a>
    
  </body>
  </html>"""

  return page

@app.route('/linktree') 
def linktree():
  page = """<!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My Linktree Website</title>
    <link href="static/linktree_style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <img src="static/images/Cat_green_eyes.png" width = 50%>
    <h1>Marta R</h1>
    <p>Learning Python is my favorite thing</p>
    <h2>Socials</h2>
    <div>
      <ul>
        <li><a href = "https://www.linkedin.com/">LinkedIn</a></li>
        <li><a href = "https://github.com/MartaReb">GitHub</a></li>
      </ul>
    </div>
  </body>
  </html>"""

  return page