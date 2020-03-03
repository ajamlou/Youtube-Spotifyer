import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
import spotify
from json.decoder import JSONDecodeError


username = "kodstuga"
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

Spotify = spotify.Spotify()

try:
    token = util.prompt_for_user_token(
        username, scope, Spotify.client_id, Spotify.client_secret, Spotify.redirect_uri)  # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(
        username, scope, Spotify.client_id, Spotify.client_secret, Spotify.redirect_uri)  # add scope

spotifyObject = spotipy.Spotify(auth=token)
