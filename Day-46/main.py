from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = os.environ["Spotify_id"]
CLIENT_SECRET = os.environ["Spotify_secret"]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", attrs={'class': ["a-no-trucate", "u-font-size-23@tablet", "lrv-u-font-size-16",
                                                  "u-line-height-125", "u-line-height-normal@mobile-max",
                                                  "a-truncate-ellipsis", "u-max-width-245",
                                                  "u-max-width-230@tablet-only", "u-letter-spacing-0028@tablet"]})
musicians = soup.find_all(name="span", attrs={'class': ["a-no-trucate", "lrv-u-font-size-14@mobile-max",
                                                        "u-line-height-normal@mobile-max", "u-letter-spacing-0021",
                                                        "a-truncate-ellipsis-2line", "u-max-width-330",
                                                        "u-max-width-230@tablet-only", "u-font-size-20@tablet"]})
songs_list = [song.getText().strip() for song in songs]
musicians_list = [musician.getText().strip() for musician in musicians]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:3000",
    scope="playlist-modify-private",
    cache_path="token.txt",
    show_dialog=True,
    username="Tarkan Gür")
    )
user_id = sp.current_user()["id"]
print(user_id)
songs_uri = []
year = date.split("-")[0]
for i in range(0, len(songs_list)):
    song = songs_list[i]
    artist = musicians_list[i]
    result = sp.search(q=f"track:{song}, year:{year}",
                       type="track")
    try:
        songs_uri.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
