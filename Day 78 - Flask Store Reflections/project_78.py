from flask import Flask

app = Flask(__name__)

my_reflections = {}

my_reflections["76"] = {"link":"https://github.com/MartaReb/100-days-of-code-Python-Replit/blob/main/Day%2076%20-%20Flask%20Web%20Server/project_76.py", "Reflection":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."}

my_reflections["77"] = {"link":"https://github.com/MartaReb/100-days-of-code-Python-Replit/blob/main/Day%2077%20-%20Flask%20Template%20For%20A%20Blog/project_77.py", "Reflection":"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}

@app.route('/')
def home():
  pages = list(my_reflections.keys())
  links = [f'<a href="/{page}">Day {page}</a>' for page in pages]
  return f"<h1>Available Reflections</h1><ul>{''.join([f'<li>{link}</li>' for link in links])}</ul>"

@app.route('/<page_number>')

def index(page_number):
  global my_reflections
  page = ""
  f = open("template/reflection.html", "r")
  page = f.read()
  f.close()

  page = page.replace("{day}", page_number)
  page = page.replace("{link}", my_reflections[page_number]["link"])
  page = page.replace("{reflection}", my_reflections[page_number]["Reflection"])
  return page

app.run(host='0.0.0.0', port=5000, debug=True)