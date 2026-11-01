#Album
def make_album(artist, title, tracks=None):
    """Return a dictionary representing an album."""
    album = {
        'artist': artist.title(), 
        'title': title.title()
        }
    if tracks:
        album['tracks'] = tracks
    return album

#membuat tiga dictionary album
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Ed Sheeran', 'Divide', tracks=12)
album3 = make_album('Adele', '25', tracks=11)
album4 = make_album('Coldplay', 'Parachutes')

#menampilkan hasil
print(album1)
print(album2)
print(album3)
print(album4)
