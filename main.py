import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="CLIENT-ID",
                                               client_secret="CLIENT-SECRET",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="USERNAME"))

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to?\nFormat: YYYY-MM-DD\n")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

top_100_songs = []
chart_result_list = soup.find_all(name="li", class_="o-chart-results-list__item")
for li in chart_result_list:
    song_titles = li.find_all(name="h3", id="title-of-a-story")
    for h3 in song_titles:
        top_100_songs.append(h3.text.strip())

song_uris = []
year = date.split("-")[0]
for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)