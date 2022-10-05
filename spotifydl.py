import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from termcolor import colored
import time
from requests import get
from youtube_dl import YoutubeDL
filename = time.strftime("%Y%m%d-%H%M%S")
os.system('color')
os.system('cls')
CLIENT_ID = "35603db6a85c4bca821afb1e71b3083c"
CLIENT_SECRET = "a5f8b634fdd446de80bd9bcf92c024a6"
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))
playlist_url = input('Input spotify playlist url: ').strip('https://open.spotify.com/playlist/')
if '?si=' in playlist_url:
    playlist_url = playlist_url.split('?')[0]
pl = sp.playlist_tracks(playlist_url)
name_list = []
print(colored('Loading tracks from playlist!','green'))
on_load_1=0
for track in pl['items']:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_genres = artist_info["genres"]
    
    #Album
    album = track["track"]["album"]["name"]
    name_list.append(f'{track_name} {artist_name}')
    tr=colored(f"Loaded Track: {track_name} - {artist_name}",'yellow')
    print(tr)
    on_load_1+=1

os.system('if exist name_artist.txt del name_artist.txt')
with open('name_artist.txt', 'a',encoding='utf-8') as names_file:
    for x in range(0,len(name_list)):
        names_file.write(f'{name_list[x]}\n')
        
##download stuffs
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True','quiet':'True'}


def search(arg):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(arg) 
        except:
            video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else:
            video = ydl.extract_info(arg, download=false)
    return video
songs=[]
urls=[]
with open('name_artist.txt') as my_file:
        tmp = my_file.readlines()
        for x in range(0,len(tmp)):
            songs.append(tmp[x].replace('\n',''))
total = len(songs)
dld=0
fn_l1 = colored(f"Done! Loaded {len(pl['items'])} songs!",'green')
print(fn_l1)
for x in range(0,len(songs)):
    urls.append(search(songs[x])['id'])
    l2 = colored(f'Searching for song urls... {x+1}/{len(songs)}','yellow')
    print(l2,end='\r',flush=True)
os.system('if not exist downloads mkdir downloads')
os.system(f'cd downloads && mkdir {filename}')
for x in range(0,len(urls)):
    dl_str = colored(str('Downloading '+str(dld)+'/'+str(total) + ' (Be patient, may be slow)'),'yellow')
    print(dl_str,end='\r',flush=True)
    os.system(f"yt-dlp -x --audio-format mp3 {'https://youtu.be/'+urls[x]} --quiet")
    dld+=1
    os.system(f'copy *.mp3 downloads\{filename} >NUL')
    os.system('del *.mp3')
os.system('del name_artist.txt')
dun = colored(f'Done! downloaded {total}/{total} songs.','green')
os.system('cls')
print(dun)
time.sleep(5)