# API endpoints:

## Base: /api/v1

<details open>
<summary>/search/<searchstring></summary>

```
> curl localhost:5000/api/v1/search/This%20Heart%20Is%20On%20Fire

[
  {
    "artist_id": 12085,
    "artist_name": "Wolf Parade",
    "artist_url": "https://www.ultimate-guitar.com/artist/wolf_parade_12085",
    "date": "1129680001",
    "id": 264702,
    "part": "",
    "preset_id": 0,
    "rating": 4.80031,
    "recording": {
      "is_acoustic": 0,
      "performance": null,
      "recording_artists": [],
      "tonality_name": ""
    },
    "song_id": 163955,
    "song_name": "This Heart Is On Fire",
    "status": "approved",
    "tab_access_type": "public",
    "tab_url": "https://tabs.ultimate-guitar.com/tab/wolf-parade/this-heart-is-on-fire-chords-264702",
    "tonality_name": "",
    "tp_version": 0,
    "type": "Chords",
    "verified": 0,
    "version": 1,
    "version_description": null,
    "votes": 10
  },
  {
    "artist_id": 12085,
    "artist_name": "Wolf Parade",
    "artist_url": "https://www.ultimate-guitar.com/artist/wolf_parade_12085",
    "date": "1129680001",
    "id": 1279705,
    "part": "",
    "preset_id": 0,
    "rating": 0,
    "recording": {
      "is_acoustic": 0,
      "performance": null,
      "recording_artists": [],
      "tonality_name": ""
    },
    "song_id": 163955,
    "song_name": "This Heart Is On Fire",
    "status": "approved",
    "tab_access_type": "public",
    "tab_url": "https://tabs.ultimate-guitar.com/tab/wolf-parade/this-heart-is-on-fire-ukulele-1279705",
    "tonality_name": "",
    "tp_version": 0,
    "type": "Ukulele Chords",
    "verified": 0,
    "version": 1,
    "version_description": null,
    "votes": 0
  }
]
```
</details>



```
Download a song:
  /api/v1/download/<url>
```

```
curl localhost:5000/api/v1/download/https://tabs.ultimate-guitar.com/tab/wolf-parade/this-heart-is-on-fire-chords-264702
{
  "id": "163955-12085",
  "tab_url": "https://tabs.ultimate-guitar.com/tab/wolf-parade/this-heart-is-on-fire-chords-264702",
  "artist_name": "Wolf Parade",
  "song_name": "This Heart Is On Fire",
  "tab_content": "[tab][ch]C[/ch]\r\nSometimes they rock and roll[/tab]\r\n[tab][ch]G[/ch]                                         [ch]Am[/ch]   [ch]F[/ch]\r\nSometimes they stay at home and it's just fine[/tab]\r\n[tab][ch]C[/ch]\r\nThis heart's on fire[/tab]\r\n[tab][ch]F[/ch]\r\nThis heart's on fire (2x)[/tab]\r\n\r\n\r\n[tab][ch]C[/ch]\r\nI am my mother's hen[/tab]\r\n[tab][ch]G[/ch]\r\nand left the body in the bed all day[/tab]\r\n[tab]               [ch]Am[/ch]     [ch]F[/ch]\r\nWe don't know what to do[/tab]\r\n[tab][ch]C[/ch]\r\nThis heart's on fire[/tab]\r\n[tab][ch]F[/ch]\r\nThis heart's on fire (2x)[/tab]\r\n\r\n[tab][ch]C[/ch]\r\nA thousand made-up loves[/tab]\r\n[tab][ch]G[/ch]                                                 [ch]Am[/ch]    [ch]F[/ch]\r\nWhat makes the sound of surf once you know you're alive?[/tab]\r\n[tab][ch]C[/ch]\r\nThis heart's on fire[/tab]\r\n[tab][ch]F[/ch]\r\nThis heart's on fire (2x)[/tab]\r\n\r\n\r\n[tab][ch]Am[/ch]                              [ch]F[/ch]\r\nIt's getting better all the time[/tab]\r\n[tab][ch]Am[/ch]                              [ch]F[/ch]\r\nIt's getting better all the time[/tab]\r\n\r\n[tab][ch]C[/ch]               [ch]F[/ch]\r\nThis heart's on fire (4x)[/tab]\r\n\r\n[tab][ch]C[/ch]\r\nAnd you're my favourite thing[/tab]\r\n[tab][ch]G[/ch]\r\ntell it everywhere I go[/tab]\r\n[tab]        [ch]Am[/ch]           [ch]F[/ch]\r\nI don't know what to do[/tab]\r\n[tab][ch]C[/ch]\r\nThis heart's on fire[/tab]\r\n[tab][ch]F[/ch]\r\nThis heart's on fire (2x)[/tab]\r\n\r\n[tab][ch]C[/ch]\r\nSometimes they rock and roll[/tab]\r\n[tab][ch]G[/ch]                                 [ch]Am[/ch]   [ch]F[/ch]\r\nI'd rather stay at home in real life[/tab]\r\n[tab][ch]C[/ch]\r\nThis heart's on fire[/tab]\r\n[tab][ch]F[/ch]\r\nThis heart's on fire (2x)[/tab]\r\n\r\n[tab][ch]Am[/ch]                          [ch]F[/ch]\r\nIt's getting better all the time (4x)[/tab]\r\n\r\n[tab][ch]C[/ch]               [ch]F[/ch]\r\nThis heart's on fire (8x)[/tab]",
  "capo_fret": 0,
  "parsed": [
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "Sometimes they rock and roll"
    },
    {
      "type": "chord",
      "content": "G                                         Am   F"
    },
    {
      "type": "text",
      "content": "Sometimes they stay at home and it's just fine"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "This heart's on fire"
    },
    {
      "type": "chord",
      "content": "F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (2x)"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "I am my mother's hen"
    },
    {
      "type": "chord",
      "content": "G"
    },
    {
      "type": "text",
      "content": "and left the body in the bed all day"
    },
    {
      "type": "chord",
      "content": "               Am     F"
    },
    {
      "type": "text",
      "content": "We don't know what to do"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "This heart's on fire"
    },
    {
      "type": "chord",
      "content": "F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (2x)"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "chord",
      "content": "A thousand made-up loves"
    },
    {
      "type": "chord",
      "content": "G                                                 Am    F"
    },
    {
      "type": "text",
      "content": "What makes the sound of surf once you know you're alive?"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "This heart's on fire"
    },
    {
      "type": "chord",
      "content": "F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (2x)"
    },
    {
      "type": "chord",
      "content": "Am                              F"
    },
    {
      "type": "text",
      "content": "It's getting better all the time"
    },
    {
      "type": "chord",
      "content": "Am                              F"
    },
    {
      "type": "text",
      "content": "It's getting better all the time"
    },
    {
      "type": "chord",
      "content": "C               F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (4x)"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "And you're my favourite thing"
    },
    {
      "type": "chord",
      "content": "G"
    },
    {
      "type": "text",
      "content": "tell it everywhere I go"
    },
    {
      "type": "chord",
      "content": "        Am           F"
    },
    {
      "type": "text",
      "content": "I don't know what to do"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "This heart's on fire"
    },
    {
      "type": "chord",
      "content": "F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (2x)"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "Sometimes they rock and roll"
    },
    {
      "type": "chord",
      "content": "G                                 Am   F"
    },
    {
      "type": "text",
      "content": "I'd rather stay at home in real life"
    },
    {
      "type": "chord",
      "content": "C"
    },
    {
      "type": "text",
      "content": "This heart's on fire"
    },
    {
      "type": "chord",
      "content": "F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (2x)"
    },
    {
      "type": "chord",
      "content": "Am                          F"
    },
    {
      "type": "text",
      "content": "It's getting better all the time (4x)"
    },
    {
      "type": "chord",
      "content": "C               F"
    },
    {
      "type": "text",
      "content": "This heart's on fire (8x)"
    }
  ]
}
```

```
List songs in the "database":
  /api/v1/songs
```

```
curl localhost:5000/api/v1/songs
[{"artist_name": "Wolf Parade", "song_name": "Dear Sons And Daughters Of Hungry Ghosts", "id": "163942-12085"}, {"artist_name": "Wolf Parade", "song_name": "This Heart Is On Fire", "id": "163955-12085"}, {"artist_name": "Mandolin Orange", "song_name": "Daylight", "id": "1683654-37156"}, {"artist_name": "Passenger", "song_name": "Let Her Go", "id": "298037-21762"}]
```


```
HTTP GET:
  Get the song json
  /api/v1/song/<id>
```
<see /download endpoint - same object>

```
HTTP POST:
  modify the song json
  /api/v1/song/<id>
```
<send as body the entire song json with edits>
returns "Success"

```
HTTP DELETE:
  delete the song
  /api/v1/song/<id>
```
returns "Success"
