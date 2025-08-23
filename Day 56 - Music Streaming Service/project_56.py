import csv, os

with open("./Day 56 - Music Streaming Service/100MostStreamedSongs.csv", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  
  for row in reader:
    try:
      os.mkdir(row["Artist(s)"])
    except FileExistsError:
      pass
      
    with open (f"{row['Artist(s)']}/{row['Song']}.txt", "w") as song_file:
      song_file.write("")