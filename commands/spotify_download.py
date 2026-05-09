import spotdl
import os
from dotenv import load_dotenv
load_dotenv()

def spotify_download(url: str):
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    secret_key = os.getenv('SPOTIFY_SECRET_KEY')
    client = spotdl.SpotifyClient.init(
        "",
        "",
        user_auth=True,
    )
    song = spotdl.Song.from_url(url=url)
    spotdl.Downloader.download_song(self=spotdl.Downloader(), song=song)
