#Function to Compare

def Compare(a,b,c):
    x = True
    if(int(a) == int(b)):
        x = True
    elif(int(b) == int(c)):
        x = True
    elif(int(c) == int(a)):
        x = True
    else:
        x = False
    return x

#Main Code
    print(Compare(3,4,3))
    print(Compare(3,4,5))
    print(Compare(77, 53, "77"))
   
        
    
