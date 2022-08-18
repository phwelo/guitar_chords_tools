#!/usr/bin/env python3

import search
import argparse
import grab_song
import chords_parser
from colorama import Fore, Style

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest="search_query", help="Song and/or Artist of song to search for")

search_results = search.get_songs_list(parser.parse_args().search_query)

for i, result in enumerate(search_results):
  if "/pro/" in result["tab_url"]:
    continue
  print(Fore.BLUE + str(i + 1), Style.RESET_ALL + result["artist_name"], Fore.BLUE + "-" + Style.RESET_ALL, result["song_name"])
  print(" " * len(str(i + 1)), Fore.LIGHTBLACK_EX + result["tab_url"] + Style.RESET_ALL)
  print("")

# should ensure that windows vt100 is used
import ctypes; kernel32 = ctypes.WinDLL('kernel32'); hStdOut = kernel32.GetStdHandle(-11); mode = ctypes.c_ulong(); kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode)); mode.value |= 4; kernel32.SetConsoleMode(hStdOut, mode)

song_number = int(input("Choose a number, champ:")) - 1
url = search_results[song_number]
song = grab_song.Song(url["tab_url"])
# print(chords_parser.parse_chords(song.tab_content))
print(song.artist_name, song.song_name)
# print("Capo:", song.capo_fret)
print("")
for line in chords_parser.parse_chords(song.tab_content):
  print(line["content"])
  # print(line)
