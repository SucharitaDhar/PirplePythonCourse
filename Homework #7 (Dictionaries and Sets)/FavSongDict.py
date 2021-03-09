FavSong = { "Genre" : "Bollywood Romance", "Composer" : "Amit Trivedi", "Lyricist" : "Amitabh Bhattacharya" , "Singer_male" : "Arijit Singh", 
            "Singer_female" : "Nikhita Gandhi", "Album" : "Kedarnath", "YearReleased" : 2018, "DurationInSeconds" : 351}
            
#Print all key value pairs
for key, value in FavSong.items() :
    print (key ,":", value)
    
#Guess Function
def Guess (Key, Value):
    if(Key in FavSong):
        if(FavSong[Key]==Value):
            return True
        else:
            return False
    else:
        return False
#Cal Guess Function after accepting input key and value        
Key = input("Enter Key :")
Value = input("Enter Value :")       
print(Guess(Key,Value))
    
