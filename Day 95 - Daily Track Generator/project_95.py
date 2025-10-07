import requests, os, json, random
from requests.auth import HTTPBasicAuth

news_key = os.getenv("NEWS_API_KEY")
country = "us"
spotify_key = os.getenv("SPOTIFY_KEY")
client_ID = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_key}"
response = requests.get(url)
data = response.json()

words = []
for article in data.get('articles', []):
    if not article.get("title"):
        continue
    try:
        word, _ = article["title"].split(" ", 1)
        words.append(word)
    except ValueError:
        continue

if len(words) > 5:
  words = random.sample(words, 5)

url = "https://accounts.spotify.com/api/token"
auth_data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_ID, client_secret)
token_response = requests.post(url, data=auth_data, auth=auth)
access_token = token_response.json()["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

songs = []
for w in words:
    query = w.strip()
    search_url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    spotify_response = requests.get(search_url, headers=headers)
    data = spotify_response.json()
    try:
        songs.append(data["tracks"]["items"][0])
    except (KeyError, IndexError):
        songs.append({"name": None, "preview_url": None})

for i in range(len(songs)):
  if songs[i]["name"] is not None:
    print(f"News word: {words[i]}")
    print(f"Song: {songs[i]['name']}")
    if songs[i]["preview_url"]:
      print(f"Preview: {songs[i]['preview_url']}")
    else:
      print(f"Spotify link: {songs[i]['external_urls']['spotify']}")
    print()