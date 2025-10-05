import requests, os

newsKey = os.getenv("NEWS_API_KEY")
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
  print(f"\nTop headlines from {country.upper()}:\n")
  for article in data.get('articles'):
    print(f"Title:{article['title']}")
    print(f"Content:{article['content']}")
    print()
else:
  print(f"Error: {data.get('message', 'Unknown error')}")