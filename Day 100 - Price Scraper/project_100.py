import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

book_info = {"book_title": "Alchemised", "my_price": 50.00}

def product_info():
  url = "https://czytam.pl/"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")
  
  products = soup.find_all("div", {"class": "product-bottom"})
  for product in products:
    title_tag = product.find("a", class_="prod-name")
    if title_tag:
      title = title_tag.get_text(strip=True)
      if title == book_info["book_title"]:
          if title_tag and title_tag.has_attr("href"):
              link = title_tag["href"] 
          else:
              link = None
          price_tag = product.find("span", class_="prod-priceValue")
          if price_tag:
            price_text = price_tag.get_text(strip=True)
            price = float(price_text.replace("zł", "").replace(",", ".").strip())
          else:
            price = None
          return link, price
  return None, None  
  
def send_email(link, price):
  password = os.environ["MAIL_PASSWORD"]
  username = os.environ["MAIL_USERNAME"]
  recipient = os.environ.get("MAIL_USERNAME", username)
  server = "poczta.o2.pl"
  port = 587
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = recipient
  msg["From"] = username
  msg["Subject"] = "The Price Has Changed!"
  body = f"""
  <h3>Book: {book_info['book_title']}</h3>
  <p>Link: <a href="{link}">{link}</a><br>
  Your price: {book_info['my_price']}<br>
  Actual price: {price}</p>"""
  msg.attach(MIMEText(body, "html"))
  s.send_message(msg)
  s.quit()
  del msg
  
def check_price():
  link, price = product_info()
  if price is not None and price <= book_info["my_price"]:
      send_email(link, price)

schedule.every().day.at("08:00").do(check_price)

while True:
  schedule.run_pending()
  time.sleep(60)