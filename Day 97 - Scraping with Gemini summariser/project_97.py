import requests
from bs4 import BeautifulSoup
from google import genai

url = input("Paste wiki URL > ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
article = soup.find_all("div", {"id": "mw-content-text"})

text = ""
for articles in article:
  content = articles.find_all("p")
  for p in content:
    text += p.text

client = genai.Client(api_key="GEMINI_API_KEY")
resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Summarize the following text in no more than 2 paragraphs:\n{text[:3000]}"
)

print(resp.text)