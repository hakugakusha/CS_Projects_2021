from lyricsgenius import Genius

genius = Genius('4Q-mvPPNijWi36HAGc3sIOyNGxWfjNaxiR68XK54mei2KjtRTIAHP7HzM_tEIpB2', skip_non_songs=True)
file = open("C:\\Users\\Brooklyn\\PycharmProjects\\Learning_Python\\Python_Projects\\lyrics.txt", "w")

artist_name = input("What artist do you want? ")
song_title = input("What song are you looking for? ")


def scrape_lyrics(artist, title):
    songs = (genius.search_song(song_title, artist_name))
    list = [songs.lyrics[:-29]]
    file.write("\n \nEnd of Lyrics".join(list))

scrape_lyrics(artist_name, song_title)
