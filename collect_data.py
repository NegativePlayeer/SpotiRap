import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# import os
from rich import print
import json

load_dotenv()
with open("data/artists.json", "r") as f:
    ARTISTS = json.load(f)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# artist = sp.search(q="Taco Hemingway", type="artist", limit=1)

# `15 character`
# artist["artists"]["items"][0]["uri"][15:]


def get_artist_albums(artist_id):
    results = sp.artist_albums(artist_id, album_type="album,single", limit=10)
    albums = results["items"]

    return albums


artist_albums = get_artist_albums(ARTISTS["Taco Hemingway"])

for i in range(len(artist_albums)):
    print(artist_albums[i]["id"], artist_albums[i]["name"])
