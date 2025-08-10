# picks random songs and plays them on spotify
# made by skel67
# allow spotify to open links in your browser
import random
import webbrowser
def list_songs():
    songs = [
        "https://open.spotify.com/track/5v2wBVnZ8Wdj1qwIqhcVw2?si=56e5b5c8c9264e64",
        "https://open.spotify.com/track/39JofJHEtg8I4fSyo7Imft?si=e8ace2f51f3a4464",
        "https://open.spotify.com/track/4NgajWFSfTQTyZsV275ZvW?si=ea38ded00e0c4d79",
        "https://open.spotify.com/track/2NZueN792gbgxi115MywKf?si=d2e668524b9e4220",
        "https://open.spotify.com/track/3ISBxX6W5NLWSVva72jtKj?si=60b937761ef046f3",
        "https://open.spotify.com/track/3Pv3UtJWZ8E3V0CG7LFFnY?si=c8d43e39905a4941",
        "https://open.spotify.com/track/6SZwj6cjc8JQbkrr8cbIUn?si=82fbdc1665334ca5",
        'https://open.spotify.com/track/0hta2Lb2zKJ7kEnAEZEE3G?si=47da0ba7325d4ba0',
        "https://open.spotify.com/track/7cEUiQ4Wc2JpU9tkzrYqfv?si=b5f15460d8da4942",
        "https://open.spotify.com/track/4wEuNvb7oG8oZYrZPZ9rPr?si=9fb8747365494483",
        "https://open.spotify.com/track/1FxmJ9hQ0nVrOI19SChpi8?si=85560d14d6bb476c5",
        "https://open.spotify.com/track/1gjAO9DiEqd7owBuN2paVI?si=89631c26d2ab43ad",
        "https://open.spotify.com/track/4Iwq23SVTkRJbWUdBXfUv9?si=15526bbe66e748d5",
        "https://open.spotify.com/track/2rUFw5MKioz2642IWt4pfu?si=TL4Y8hP4Tr-HHIKoEWefJw"
        
    ]
    return songs
def random_song_on_spotify():
    songs = list_songs()
    random_song = random.choice(songs)
    webbrowser.open(random_song)
    return random_song
if __name__ == "__main__":
    print("Opening a random song on Spotify...")
    song = random_song_on_spotify()
    print(f"Now playing: {song}")