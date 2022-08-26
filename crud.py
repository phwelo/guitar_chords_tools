#!/usr/bin/env python3
from flask import Flask, request
from search import get_songs_list as song_query
from grab_song import Song
import os, json

app = Flask(__name__)

home_directory = os.path.expanduser( '~' )
storage_path = os.path.join( home_directory, 'Guitar Songs' )

def init():
  os.makedirs(storage_path, exist_ok=True)

def write_song(song):
  with open(os.path.join(storage_path, song.id + ".json"), "w", encoding="utf-8") as f:
    f.write(str(json.dumps(song.__dict__)))

@app.route('/')
def hello_world():
  return 'This should probably be a help page or documentation of some sort.'

@app.route('/api/v1/search/<query>')
def search_songs(query):
  return song_query(query)

@app.route('/api/v1/download/<path:url>')
def download_song(url):
  song = Song(url)
  write_song(song)
  return json.dumps(song.__dict__)

@app.route('/api/v1/songs')
def list_songs():
  songs = []
  for file in  os.listdir(storage_path):
    with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
      result = json.loads(f.read())
      songs.append({
        "artist_name": result["artist_name"],
        "song_name": result["song_name"],
        "id": result["id"]
      })
  return json.dumps(songs)

@app.route('/api/v1/song/<id>', methods = ['PUT', 'GET'])
def song_info(id):
  if request.method == 'GET':
    with open(os.path.join(storage_path, id + ".json"), "r", encoding="utf-8") as f:
      return f.read()
  elif request.method == 'PUT':
    with open(os.path.join(storage_path, id + ".json"), "w", encoding="utf-8") as f:
      f.write(request.data)
    return "Success"


if __name__ == '__main__':
  init()
  app.run(debug=True)
