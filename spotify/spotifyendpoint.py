import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
import spotify
from json.decoder import JSONDecodeError


username = "kodstuga"
scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private'

Spotify = spotify.Spotify()

try:
    token = util.prompt_for_user_token(
        username, scope, Spotify.client_id, Spotify.client_secret, Spotify.redirect_uri)  # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(
        username, scope, Spotify.client_id, Spotify.client_secret, Spotify.redirect_uri)  # add scope

spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
displayName = user['display_name']
followers = followers = user['followers']['total']

while True:
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print("2 - add playlist")
    print("3 - add song to playlist")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        query = input("Alright beach! What is the name of the artist?: ")
        searchResults = spotifyObject.search(query, 1, 0, "artist")
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()

    if choice == "1":
        break

    if choice == "2":
        name = input("Okey mateyo what is the name of the playlist? ")
        spotifyObject.user_playlist_create(user["id"], name)

    if choice == "3":
        query_song = input("Okey dude. What is the name of the song? ")
        query_artist = input("Okey dude. What is the artist of the song? ")
        searchResults = spotifyObject.search(
            q='artist:'+query_artist+' track:'+query_song)
        song_uri = searchResults['tracks']['items'][0]['uri']
        playlist = spotifyObject.user_playlists(user['id'])['items'][0]['id']
        spotifyObject.user_playlist_add_tracks(
            user['id'], playlist_id=playlist, tracks=[song_uri])
