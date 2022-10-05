# Spotify-DL

A simple spotify to youtube converter built for windows.

## Installation

You need to install the [YT-DLP EXE](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe) for windows as well as [ffmpeg](https://ffmpeg.org/download.html), and add them to path for everything to run properly.

Also, some packages on pip are needed. Run this to get them:
```bat
pip install -r requirements.txt
```
Finally, fill in the forms on lines 11 & 12 with the respective data.
```
CLIENT_ID=id
CLIENT_SECRET=secret
```
To fill these in, go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an application. In this you can find the info you need to fill out the data above.
## Usage

```
Simply run the spotify.py file and it will prompt you for a playlist url (ex:https://open.spotify.com/playlist/37i9dQZF1EIcACGtnmfS1M?si=1b2d4bd3c893497a)
Paste this in and hit enter. It will then do everything else. Just wait for it to close and check the downloads folder!
```




## License
[Apache](https://www.apache.org/licenses/LICENSE-2.0)
