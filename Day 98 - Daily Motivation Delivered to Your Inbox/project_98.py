import schedule, time, random, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open("quotes.txt", "r", encoding="utf-8") as f:
  quotes = f.read().splitlines()

password = os.environ["MAIL_PASSWORD"]
username = os.environ["MAIL_USERNAME"]
recipient = os.environ.get("MAIL_USERNAME", username)

def sendMail():
  quote = random.choice(quotes)
  print(quote)
  server = "poczta.o2.pl"
  port = 587
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = recipient
  msg["From"] = username
  msg["Subject"] = "Daily Inspiration"
  body = f"<h3>{quote}</h3>✨</p>"
  msg.attach(MIMEText(body, 'html'))

  s.send_message(msg)
  s.quit()
  del msg

schedule.every().day.at("08:00").do(sendMail)

while True:
  schedule.run_pending()
  time.sleep(1)
