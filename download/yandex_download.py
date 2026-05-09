from yandex_music import Client

def yandex_download(url: str, yandex_oauth: str):
    client = Client(yandex_oauth).init()
    track_id = url.split('/track/')[1].split('?')[0]

    track = client.tracks(track_id)[0]
    artists = ', '.join([artist.name for artist in track.artists])

    track.download(f'{artists} - {track.title}.mp3')