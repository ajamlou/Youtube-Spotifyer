import os
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

song = 'bara du'
artist = 'kasbo'


class add_songs_to_spotify:


    client_id = "6cb010cfc3774f8ca5247a501664a548"
    client_secret = "d99c3963895a4f029e1829443ff7b9e9"
    redirect_uri = "https://google.com/"
    username = "kodstuga"
    scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private'


    try:
        token = util.prompt_for_user_token(
            username, scope, client_id, client_secret, redirect_uri)  # add scope
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(
            username, scope, client_id, client_secret, redirect_uri)  # add scope

    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
    displayName = user['display_name']
    followers = followers = user['followers']['total']

    def add_songs(self, song, artist):
        query_song = song
        query_artist = artist
        search_results = self.spotifyObject.search(
            q='artist:' + query_artist + ' track:' + query_song)
        print('A')
        try:
            song_uri = search_results['tracks']['items'][0]['uri']
            playlist = self.spotifyObject.user_playlists(self.user['id'])['items'][0]['id']
            self.spotifyObject.user_playlist_add_tracks(
                self.user['id'], playlist_id=playlist, tracks=[song_uri])
        except (IndexError):
            print('Song or artist was not found.')

#add_songs_to_spotify().add_songs('dhwkjeh', 'ewrerrwe')

    # while True:
    #     print()
    #     print(">>> Welcome to Spotipy " + displayName + "!")
    #     print(">>> You have " + str(followers) + " followers.")
    #     print()
    #     print("0 - Search for an artist")
    #     print("1 - exit")
    #     print("2 - add playlist")
    #     print("3 - add song to playlist")
    #     print()
    #     choice = input("Your choice: ")
    #
    #     if choice == "0":
    #         query = input("Alright beach! What is the name of the artist?: ")
    #         searchResults = spotifyObject.search(query, 1, 0, "artist")
    #         artist = searchResults['artists']['items'][0]
    #         print(artist['name'])
    #         print(str(artist['followers']['total']) + " followers")
    #         print(artist['genres'][0])
    #         print()
    #
    #     if choice == "1":
    #         break
    #
    #     if choice == "2":
    #         name = input("Okey mateyo what is the name of the playlist? ")
    #         spotifyObject.user_playlist_create(user["id"], name)


