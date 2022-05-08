from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from youtube_dl import YoutubeDL
from termcolor import colored
import time
import numpy as np
from queue import Queue
import threading
os.system('color')
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))
def download(url,filename):
	os.system(f"cd downloads\{filename} && yt-dlp -x --audio-format mp3 {url} --quiet")
YDL_OPTIONS = {'format':'bestaudio','noplaylist':'True','quiet':'True'}
def search(arg):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(arg) 
        except:
            video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else:
            video = ydl.extract_info(arg, download=false)
    return 'https://youtu.be/'+video['id']

def download_thread(url,filename,q,total,tnum):
	for x in range(0,len(url)):
		on_now = q.get()
		print(f'Downloading... {on_now+1}/{total}',end='\r',flush=True)
		q.put(on_now + 1)
		os.system(f"cd downloads\{filename} && yt-dlp -x --audio-format mp3 {url[x]} --quiet")


class misc:
	def create_folder(filename):
		os.system('if not exist downloads mkdir downloads')
		os.system(f'cd downloads && mkdir {filename}')
	def chunk_arr(arr,chunks):
		chunked = np.array_split(arr,chunks)
		return(chunked)





class searcher:
	def search_sp(url):
		if 'https://open.spotify.com/playlist/' in url:
			url = url.strip('https://open.spotify.com/playlist/')
			if '?si=' in url:
				url = url.split('?')[0]
			data = sp.playlist_tracks(url)
			name_list=[]
			for track in data['items']:
				track_name = track["track"]["name"]
				artist_name = track["track"]["artists"][0]["name"]
				name_list.append(f'{track_name} {artist_name}')
			return(name_list)
		
		elif 'https://open.spotify.com/track/' in url:
			url = url.strip('https://open.spotify.com/track/')
			data = sp.track(url)
			return(f'{data["name"]} {data["artists"][0]["name"]}')
		
		else:
			print('Invalid url passed to spotify_searcher.')


	
	
	def search_yt(inp):
		if type(inp) != str:
			urls = []
			for x in range(0,len(inp)):
				found = search(inp[x])
				urls.append(found)
				print(f'Searching youtube for urls... {x+1}/{len(inp)}',end='\r',flush=True)
			print(f'Search complete! {len(inp)} Urls found.                                      ')
			return(urls)
		else:
			return(search(inp))
			print('Search complete! 1 Url found.')


class downloader:
	def download_slow(inp,filename):
		if type(inp) == str:
			download(inp,filename)
			print(f'Download complete! 1/1')
		else:
			for x in range(0,len(inp)):
				print(f'Downloading... {x+1}/{len(inp)}',end='\r',flush=True)
				download(inp[x],filename)
			print(f'Download complete! {len(inp)}/{len(inp)}')
				
	def download_fast(inp,threads_num,filename): #should be 5 or less threads.
		if threads_num > 5:
			error_num = colored(f'ERROR: {threads_num}','red')
			error_thread = colored('threads were requested, but the max is 5. Correcting to max.','yellow')
			print(f'{error_num} {error_thread}')
			threads_num = 5
		if type(inp) != list or threads_num > len(inp):
			print(f'Error with received data. The input is less then the desired thread count of {threads_num}')
			exit()
		splitted = misc.chunk_arr(inp,threads_num)
		threads = []
		queue = Queue()
		queue.put(0)
		for x in range(0,threads_num):
			arr_work = list(splitted[x])
			threads.append(threading.Thread(target=download_thread,args=(arr_work,filename,queue,len(inp),len(threads))))
		for x in range(0,len(threads)):
			threads[x].start()
		for x in range(0,len(threads)):
			threads[x].join() 