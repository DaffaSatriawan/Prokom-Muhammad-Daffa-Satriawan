#user album
def make_album(artist, title, tracks=None):
    """Return a dictionary representing an album."""
    album = {
        'artist': artist.title(), 
        'title': title.title()
        }
    if tracks:
        album['tracks'] = tracks
    return album

#mengambil input dari pengguna
artist_name = input("Enter the artist's name: ")
album_title = input("Enter the album's title: ")
track_count = input("Enter the number of tracks (optional): ")

#membuat album berdasarkan input pengguna
if track_count:
    user_album = make_album(artist_name, album_title, tracks=int(track_count))
else:
    user_album = make_album(artist_name, album_title)

#menampilkan hasil
print(user_album)
