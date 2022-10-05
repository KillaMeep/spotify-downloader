# Spotify-DL

A simple script to download spotify songs as mp3s!

## Installation

You need to install the [YT-DLP EXE](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe) for windows as well as [ffmpeg](https://ffmpeg.org/download.html), and add them to path for everything to run properly.

Also, some packages on pip are needed. Run this to get them:
```bat
pip install -r requirements.txt
```
Finally, fill in the variables on lines 11 & 12 with the respective data.
```
CLIENT_ID=id
CLIENT_SECRET=secret
```
To fill these in, go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an application. In this you can find the info you need to fill out the data above.
## Usage

Simply run the spotify.py file and it will prompt you for a playlist url 
To find the url, follow this image:
![Url example](/examples/share.png)

This will copy the playlist URL to your clipboard. Paste this into the program when asked, and it will then do everything else for you. Just wait for the window to close and check the downloads folder!





## License
[Apache](https://www.apache.org/licenses/LICENSE-2.0)
