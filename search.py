#!/usr/bin/python3

import requests
import json
from bs4 import BeautifulSoup

search_url = "https://www.ultimate-guitar.com/search.php?search_type=title&value="

def web_search(song_name):
  r = requests.get(search_url + song_name)
  return r.text

def convert_to_json(html):
  soup = BeautifulSoup(html, 'html.parser')
  jstore = soup.find_all('div', attrs={'class': 'js-store'})[0]["data-content"]
  return json.dumps(json.loads(jstore)["store"]["page"]["data"]["results"])

def get_songs_list(song_name):
  web_result = web_search(song_name)
  results_json = convert_to_json(web_result)
  return json.loads(results_json)

def main():
  print(get_songs_list("Moonshiner"))

if __name__ == "__main__":
  main()

