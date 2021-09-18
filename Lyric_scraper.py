from lyricsgenius import Genius

genius = Genius('4Q-mvPPNijWi36HAGc3sIOyNGxWfjNaxiR68XK54mei2KjtRTIAHP7HzM_tEIpB2', skip_non_songs = True, remove_section_headers = True)
file = open("C:\\Users\\Brooklyn\\PycharmProjects\\Learning_Python\\Python_Projects\\lyrics.txt", "w")

artist_name = input("What artist do you want? ")
song_title = input("What song are you looking for? ")

song = genius.search_song(song_title, artist_name)
file.write(song.lyrics + "\n End of Lyrics")



