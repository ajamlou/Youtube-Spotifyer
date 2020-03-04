# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
import os
from os import path

import spotify.spotifyendpoint
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import csv
import time
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
csv_header = ["video_ID",
              "video_title"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    big_dic = {}

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_703029965562-lq426l0o1etgnpu3lkql5t4o28j9rk9t.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,contentDetails",
        myRating="like",
        maxResults=50
    )
    response = request.execute()
    # python = json.JSONDecoder(response)

    print(response)

    items = response["items"]

    for item in items:
        big_dic[item["id"]] = big_dic.get((item["id"], item["snippet"]["title"]), [])

    try:
        next_token = response["nextPageToken"]
    except KeyError:
        next_token = None

    while(next_token != None):
        request = youtube.videos().list(
            part="snippet,contentDetails",
            myRating="like",
            maxResults=50,
            pageToken = next_token
        )
        response = request.execute()
        items = response["items"]
        for item in items:
            big_dic[item["id"]] = big_dic.get((item["id"], item["snippet"]["title"]), [])
        try:
            next_token = response["nextPageToken"]
        except KeyError:
            next_token = None
    while True:
        print("in endless loop")
        request = youtube.videos().list(
            part="snippet,contentDetails",
            myRating="like",
            maxResults=10,
        )
        response = request.execute()
        items = response["items"]
        for item in items:
            if item["id"] not in big_dic:
                big_dic[item["id"]] = big_dic.get((item["id"], item["snippet"]["title"]), [])
                video_name = item["snippet"]["title"]
                split_video_name = video_name.split(' - ') #[ARTIST, LÅTNAMN]
                spotify.spotifyendpoint.add_songs_to_spotify().add_songs(split_video_name[1], split_video_name[0])
        time.sleep(30)
    print("existed endless oop")




if __name__ == "__main__":
    main()