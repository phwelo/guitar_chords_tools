#!/usr/bin/env python3

import argparse, os, re
import search, grab_song
from colorama import Fore, Style

def init():
  windows_handler()

def setup_vt100():
  import ctypes; kernel32 = ctypes.WinDLL('kernel32'); hStdOut = kernel32.GetStdHandle(-11); mode = ctypes.c_ulong(); kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode)); mode.value |= 4; kernel32.SetConsoleMode(hStdOut, mode)

def parse_query():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    dest="search_query", 
    help="Song and/or Artist of song to search for"
  )
  return parser.parse_args().search_query

def print_option_line(num, artist, song, url):
  print(Fore.CYAN + str(num) + ") " + \
    Fore.WHITE + artist + Fore.LIGHTBLACK_EX + \
      " - " + Fore.LIGHTCYAN_EX + song + \
        Style.RESET_ALL)
  print(" " * len(str(num)), Fore.LIGHTBLACK_EX + url + Style.RESET_ALL)
  print("")

def colorize_line(line):
  if line["type"] == "chord":
    return Fore.CYAN + line["content"] + Style.RESET_ALL
  elif line["type"] == "section":
    return "\r\n" + Fore.LIGHTBLACK_EX + line["content"] + Style.RESET_ALL + "\r\n"
  elif line["type"] == "preface":
    return Fore.LIGHTCYAN_EX + line["content"] + Style.RESET_ALL
  elif line["type"] == "tab":
    return Fore.BLUE + line["content"] + Style.RESET_ALL
  elif line["type"] == "text":
    return Fore.WHITE + line["content"] + Style.RESET_ALL
  else:
    return line["content"]

def show_choices(query_results):
  query_results = remove_chordpro(query_results)
  os.system("cls")
  [
    print_option_line(
      i + 1, 
      result["artist_name"], 
      result["song_name"], 
      result["tab_url"]
    ) for i, result in enumerate(query_results)
  ]

remove_chordpro = lambda query_results: [
    result for result in query_results if "/pro/" not in result["tab_url"] and "guitar-pro" not in result["tab_url"]
  ]
windows_handler = lambda : setup_vt100() if os.name == "nt" else None

def tab_color(line):
  line = Fore.CYAN + line
  return re.sub("-", Fore.LIGHTBLACK_EX + "-" + Fore.CYAN, line)

def output_lines(lines):
  for line in lines:
    if line["type"] == "tab":
      for tabline in line["content"]:
        print(tab_color(tabline))
    else:
      print(colorize_line(line))

def query_user():
  search_results = search.get_songs_list(parse_query())
  show_choices(search_results) # Display the results
  song_number = int(input("Choose a number, champ:")) - 1
  return search_results[song_number]["tab_url"]

def print_song(song):
  # print(song.tab_content)
  # exit()
  os.system("cls")
  print(Fore.LIGHTCYAN_EX + song.artist_name + Style.RESET_ALL)
  print(Fore.CYAN + song.song_name)
  print("")
  output_lines(song.parsed)

def main():
  init()
  tab_url = query_user()
  song = grab_song.Song(tab_url)
  print_song(song)

if __name__ == "__main__":
  main()