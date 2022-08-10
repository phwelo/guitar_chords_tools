#!/usr/bin/env python3

# Use this logic in whatever gui consumes the search results

import search
import argparse
import grab_song
import chords_parser

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest="search_query", help="Song and/or Artist of song to search for")

search_results = search.get_songs_list(parser.parse_args().search_query)

for i, result in enumerate(search_results):
  print(str(i + 1), result["artist_name"], result["song_name"])
  print(" " * len(str(i + 1)), result["tab_url"])
  print("")

song_number = int(input("Choose a number, champ:")) - 1
url = search_results[song_number]
song = grab_song.Song(url["tab_url"])
print(song.artist_name, song.song_name)
print("Capo:", song.capo_fret)
print(song.tab_content)