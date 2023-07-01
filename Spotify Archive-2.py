#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install spotipy


# In[10]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


# In[1]:


CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "REDIRECT_URI"
USER_ID = "YOUR_USER_ID"


# In[19]:


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope))


# In[57]:


with open("saved_tracks.txt", mode="a+") as file:
    for i in range(0, 587):

        result = sp.current_user_saved_tracks(limit=1, offset=i)
        track = result['items'][0]['track']
        file.write(str(i+1)+" - "+track['artists'][0]['name']+" – "+track['name']+"\n")


# In[74]:


def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# In[123]:


os.mkdir("Playlists")
os.chdir("Playlists")
playlists = sp.user_playlists(USER_ID)

for i, playlist in enumerate(playlists['items']): 
    tracks = get_playlist_tracks(USER_ID, playlist['id']) 
    try:
        with open(playlist['name']+".txt", mode="w") as file:
            for index, track in enumerate(tracks):
                artist = track["track"]["artists"][0]["name"]
                track_ = track["track"]["album"]["name"]
                file.write(str(index)+" - "+artist+" - "+track_+"\n")
            file.close()
    except:
        print("Failed to create file, please be careful that your playlist don't include '/' character")
        continue
    finally:
        os.chdir(os.pardir)


# In[ ]:




