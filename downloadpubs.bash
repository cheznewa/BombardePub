mkdir pubs
cd pubs
youtube-dl --playlist-end 100 -i --exec "ffmpeg -i {} -vf scale=320x240 {}.gif;rm {}" https://www.youtube.com/c/PubT%C3%A9l%C3%A9/videos