import spotdl

def spotify_download(url: str, client_id: str, secret_key: str):
    spotdl.SpotifyClient.init(
        client_id=client_id,
        client_secret=secret_key,
        user_auth=True,
    )

    song = spotdl.Song.from_url(url=url)
    spotdl.Downloader.download_song(self=spotdl.Downloader(), song=song)