#Genre Function
def Genre():
    return "Pop"

#Artist Function    
def Artist():
    return "Lauv"
    
#Year Function
def Year():
    return 2017
    
#Boolean Function
def CheckAvailability(song):
    return (song == 'I Like Me Better')

 
#Main Code
FavSong = "I Like Me Better"   
print("My favorite song is "+ FavSong)
print("Genre: ", Genre())
print("Artist: ", Artist())
print("Year Released: ", Year())
print("Available on Spotify: ", CheckAvailability(FavSong))


    
    
