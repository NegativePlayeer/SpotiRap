# import json
# import spotipy
# from dotenv import load_dotenv
# from spotipy.oauth2 import SpotifyClientCredentials

# load_dotenv()


# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# ARTISTS = {
#     "Taco Hemingway": "",
#     "Mata": "",
#     "Otsochodzi": "",
#     "OKI": "",
#     "White 2115": "",
#     "Bedoes": "",
#     "Chivas": "",
#     "ReTo": "",
#     "Szpaku": "",
#     "Beteo": "",
#     "Belmondodawg": "",
#     "Kubi Producent": "",
#     "Białas": "",
#     "Young Igi": "",
#     "Young Leosia": "",
#     "Quebonafide": "",
# }


# def get_artists_id():
#     for artist in ARTISTS.keys():
#         spotify_artist = sp.search(q=artist, type="artist", limit=1)

#         ARTISTS[artist] = spotify_artist["artists"]["items"][0]["uri"][15:]

#     with open("artists.json", "w") as f:
#         json.dump(ARTISTS, f)


# get_artists_id()
