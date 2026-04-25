'''

1) Read the dataset. Use kaggle.com, for instance
2) Most common artist
3) Find hitmaker/loser (artist)
4) Most feat. person
5) Top 10 genres by weightened popularity

'''

import csv

artist_counts = {}
unique_rows = set()

with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row_tuple = (row['artists'], row['track_id'], row['track_name'], row['track_genre'])
        unique_rows.add(row_tuple)
        
for row in unique_rows:
    artist = row[0]
    if artist in artist_counts:
        artist_counts[artist] += 1
    else:
        artist_counts[artist] = 1

sorted_artists = sorted(artist_counts.items(), key=lambda item: item[1], reverse=True)

n = int(input("Enter the number N: "))
for artist_name, count in sorted_artists[:n]:
    print(f"{artist_name}: {count}")
