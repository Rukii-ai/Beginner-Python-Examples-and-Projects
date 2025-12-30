def make_album(artist_name, album_title, number_of_songs = None):
    """Return a dictionary representing a music album."""
    album = {'Artist' : artist_name.title(), 'Title' : album_title.title()}
    if number_of_songs:
        album["Songs"] = number_of_songs
    return album


while True:
    print("\nEnter your favourite artist's name and favourite album!")
    print("(Enter 'q' to quit)")

    art_name = input("\nArtist Name: ")
    if art_name.lower().strip() == "q":
        break

    alb_title = input("\nAlbum Title: ")
    if alb_title.lower().strip() == "q":
        break

    song_number = input("\nNumber of Songs in album: ")
    if song_number == "q":
        break
    elif song_number.isdigit() == False:
        print("\nPlease enter valid input for number of songs!")
        continue #To stop and restart the loop

    album = make_album(art_name, alb_title, song_number)
    print(album)