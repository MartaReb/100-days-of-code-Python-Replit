import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/newest"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

my_links = soup.find_all("span", {"class": "titleline"})

things = ["python", "ai"]

for link in my_links:
  text = link.text
  text_list = text.split()
  for word in text_list:
    if word.lower() in things:
      print(link.text)
      my_link = link.find_all("a")
      print(my_link[0]["href"])
      print()