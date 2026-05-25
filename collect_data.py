import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# import os
from rich import print
import json
import time
import pandas as pd
from spotify_scraper import SpotifyClient

load_dotenv()
with open("data/artists.json", "r") as f:
    ARTISTS = json.load(f)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


def get_artist_albums(artist_id):
    results = sp.artist_albums(artist_id, album_type="album,single", limit=10)
    albums = results["items"]

    return albums


# def create_artist_data(artist_albums, artist_name):
#     tracks = {}
#     tracks_list = []

#     for i in range(len(artist_albums)):
#         tracks[artist_albums[i]["name"]] = sp.album_tracks(
#             artist_albums[i]["id"], limit=15
#         )
#         time.sleep(2)

#         # print(
#         #     [
#         #         track["duration_ms"] / 60000
#         #         for track in tracks[artist_albums[i]["name"]]["items"]
#         #     ]
#         # )

#         for track in tracks[artist_albums[i]["name"]]["items"]:
#             track_min = track["duration_ms"] / 60000

#             tracks_list.append(
#                 {
#                     "track_id": track["id"],
#                     "name": track["name"],
#                     "duration_min": round(track_min, 2),
#                     "explicit": track["explicit"],
#                     "track_number": track["track_number"],
#                     "album": artist_albums[i]["name"],
#                     "artist": artist_name,
#                     "release_date": artist_albums[i]["release_date"],
#                     "album_type": artist_albums[i]["album_type"],
#                     "total_tracks": artist_albums[i]["total_tracks"],
#                 }
#             )

#     return tracks_list


# tracks_list = []

# for artist in ARTISTS:
#     artist_albums = get_artist_albums(artist_id=ARTISTS[artist])
#     time.sleep(2)
#     tracks_list.extend(
#         create_artist_data(artist_albums=artist_albums, artist_name=artist)
#     )
#     time.sleep(2)

# df = pd.DataFrame(tracks_list)
# df.to_csv("data/tracks.csv", index=False)

# df = pd.read_csv("data/tracks.csv")
# list_of_ids = df["track_id"].tolist()

# chunk_size = 50
# track_by_popularity = {}

# for i in range(0, len(list_of_ids), chunk_size):
#     chunk = list_of_ids[i : i + chunk_size]
#     results = sp.tracks(tracks=chunk)
#     track_by_popularity.update(
#         {track["id"]: track["popularity"] for track in results["tracks"]}
#     )

# df["popularity"] = df["track_id"].map(track_by_popularity)

# print(df[["name", "popularity"]].head())

# Since spotify api blocks the scraping of popularity - however... I won't stop

# df_tracks = pd.read_csv("data/tracks.csv")
# df_plays = pd.read_csv("data/play_counts.csv")

# df_tracks["track_url"] = df_tracks["track_id"].apply(
#     lambda x: f"https://open.spotify.com/track/{x}"
# )

# df_merged = df_tracks.merge(
#     df_plays[["track_url", "play_count"]], on="track_url", how="left"
# )

# df_merged.to_csv("data/tracks.csv", index=False)
# print(df_merged[["name", "play_count"]].head(10))
