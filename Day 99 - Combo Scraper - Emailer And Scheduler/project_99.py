import requests, schedule, time, random, os, smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


interests = ["python", "hacking"]


def get_links():
    url = "https://crossweb.pl/wydarzenia/it/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    my_links = soup.find_all("a", {"class": "clearfix"})


    saved_links = set()
    if os.path.exists("events.txt"):
        with open("events.txt", "r", encoding="utf-8") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned:            
                    saved_links.add(cleaned)

    new_links = []

    for link in my_links:
        text = link.get_text(strip=True).lower()
        href = link.get("href")
        full_url = f"https://crossweb.pl{href}"

        found = False
        for interest in interests:
            if interest in text:
                found = True
                break  

        if found:
            if full_url not in saved_links:
                with open("events.txt", "a", encoding="utf-8") as f:
                    f.write(full_url + "\n")
                new_links.append(full_url)
    return new_links

def send_email(new_links):
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
    msg["Subject"] = "New Interesting Event"
    if new_links:
        body = "<br>".join(new_links)
        msg.attach(MIMEText(body, 'html'))
        print(f"Sent {len(new_links)} new events.")
    else:
        body = "No new events today"
        msg.attach(MIMEText(body, 'html'))
        print("No new events today, sent info email.")
    msg.attach(MIMEText(body, 'html'))
    s.send_message(msg)
    s.quit()
    del msg

def job():
    new_links = get_links()
    send_email(new_links)

schedule.every().day.at("08:00").do(job)
full_url = get_links()

while True:
  schedule.run_pending()
  time.sleep(1)
