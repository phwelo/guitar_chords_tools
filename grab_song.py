#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup

input_url = "https://tabs.ultimate-guitar.com/tab/steve-earle/copperhead-road-chords-1861944"

class Song:
  def __init__(self, tab_url):
    jstore = self.jstore_dump(tab_url)
    self.tab_url = tab_url
    self.artist_name = jstore["store"]["page"]["data"]["tab"]["artist_name"]
    self.song_name = jstore["store"]["page"]["data"]["tab"]["song_name"]
    self.tab_content = jstore["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
    self.capo_fret = self.capo_handler(jstore)

  def capo_handler(self, jstore):
    if "capo" in jstore["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]:
      return jstore["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]["capo"]
    else:
      return 0
  
  def jstore_dump(self, url):
    html = get_tab_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    jstore = json.loads(
      soup.find_all(
        'div',
        attrs={
          'class': 'js-store'
        }
      )[0]["data-content"]
    )
    return jstore

def get_tab_page(url):
  r = requests.get(url)
  return r.text

def main():
  song = Song(input_url)
  print(json.dumps(song.__dict__))

if __name__ == "__main__":
  main()