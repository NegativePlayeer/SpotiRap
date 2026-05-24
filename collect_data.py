import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# import os
from rich import print
import json
import time
import pandas as pd

load_dotenv()
with open("data/artists.json", "r") as f:
    ARTISTS = json.load(f)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


def get_artist_albums(artist_id):
    results = sp.artist_albums(artist_id, album_type="album,single", limit=10)
    albums = results["items"]

    return albums


def create_artist_data(artist_albums):
    tracks = {}
    tracks_list = []

    for i in range(len(artist_albums)):
        tracks[artist_albums[i]["name"]] = sp.album_tracks(
            artist_albums[i]["id"], limit=15
        )

        # print(
        #     [
        #         track["duration_ms"] / 60000
        #         for track in tracks[artist_albums[i]["name"]]["items"]
        #     ]
        # )

        for track in tracks[artist_albums[i]["name"]]["items"]:
            tracks_list.append(
                {
                    "name": track["name"],
                    "duration_ms": track["duration_ms"] / 60000,
                    "explicit": track["explicit"],
                    "track_number": track["track_number"],
                    "album": artist_albums[i]["name"],
                }
            )

        return tracks_list


tracks_list = []

# for artist in ARTISTS:
#     artist_albums = get_artist_albums(artist_id=ARTISTS[artist])
#     time.sleep(2)
#     tracks_list.extend(create_artist_data(artist_albums=artist_albums))
#     time.sleep(2)

df = pd.DataFrame(tracks_list)
df.to_csv("data/tracks.csv", index=False)
