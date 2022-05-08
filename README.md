# Spotify-DL

A simple spotify to youtube converter built for windows.

## Installation

You need to install the [YT-DLP](https://github.com/yt-dlp/yt-dlp) program for windows as well as [ffmpeg](https://ffmpeg.org/download.html), and add them to path for everything to run properly.

Also, some packages on pip are needed. Run this to get them:
```bat
pip install -r requirements.txt
```
Finally, create a file called ```.env``` and format it like this:
```
CLIENT_ID=id
CLIENT_SECRET=secret
```
To fill these in, go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an application. In this you can find the info you need to fill out the data above.
## Usage

```python
from utils.helper import *

# returns a song and artist name(s) from a Spotify playlist url/song url as an array.
songs_data = searcher.search_sp('https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT?si=d3a28aa54f8e4dd5')

# returns a YouTube url from a song name and artist. Can work with a string or array.
song_url = searcher.search_yt('Never Gonna Give You Up Rick Astley')

# Example of how to use the slow downloader:
import time
filename = time.strftime("%Y%m%d-%H%M%S") # Creates subfile name. EX: \downloads\{filename}
misc.create_folder(filename) # Creates the folders and subfiles for the downloader to run in.
downloader.download_slow(song_url,filename)# you have to pass the array/string of the url(s) to the downloader
                                           # also, pass the filename to the downloader to make sure it works.

# Example of how to use the fast(threaded) downloader:
import time
filename = time.strftime("%Y%m%d-%H%M%S") # Creates subfile name. EX: \downloads\{filename}
misc.create_folder(filename) # Creates the folders and subfiles for the downloader to run in.
threadsnum = 3 # How many threads to run on, can be from 1 to 5.
downloader.download_fast(song_urls,threadsnum,filename) # the fast downloader needs the array of song urls,
                                                        # as well as how many threads to run on and the filename.


```




## License
[Apache](https://www.apache.org/licenses/LICENSE-2.0)
