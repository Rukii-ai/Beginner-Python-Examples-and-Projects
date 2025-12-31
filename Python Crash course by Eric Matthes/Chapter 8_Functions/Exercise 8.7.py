def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary representing a music album."""
    album = {'Artist' : artist_name.title(), 'Title' : album_title.title()}
    
    if number_of_songs:
        album["Songs"] = number_of_songs
    return album


musician1 = make_album('wizkid', 'made in lagos')
musician2 = make_album(artist_name='davido', album_title='a better time')
musician3 = make_album(album_title='Sound of Heaven', 
                       artist_name='Danney Gokey')

print(musician1)
print(musician2)
print(musician3)

musician4 = make_album('Burnaboy', 'Twice as Tall', number_of_songs=15)
print(musician4)