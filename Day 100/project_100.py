import requests
from bs4 import BeautifulSoup

url = "https://czytam.pl/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all("div", {"class": "product-bottom"})

for product in products:
  title_tag = product.find("a", class_="prod-name")
  if title_tag:
    title = title_tag.get_text(strip=True)
  else:
    title = None

  if title == "Alchemised":
      if title_tag and title_tag.has_attr("href"):
          link = title_tag["href"]
      else:
          link = None
        
      price_tag = product.find("span", class_="prod-priceValue")
      if price_tag:
        price = price_tag.get_text(strip=True)
      else:
        price = None

      print("Title:", title)
      print("Link:", link)
      print("Price:", price)



