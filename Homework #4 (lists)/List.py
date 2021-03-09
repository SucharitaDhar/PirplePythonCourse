myUniqueList = []
myLeftovers = []

def addToList(item):
    if item in myUniqueList:
        addToLeftovers(item)
        return False
    else:
        myUniqueList.append(item)
        return True

def addToLeftovers(item):
  myLeftovers.append(item)

# Testing the addToList function
print(myUniqueList) #[]
print(addToList("pizza")) # Returns True
print(myUniqueList) # ['pizza']
print(myLeftovers) # []
# Adding the element that already exists
print(addToList("pizza")) # Returns False
print(myUniqueList) # ['pizza']
print(myLeftovers) # ['pizza']
# Adding a new element
print(addToList("burger")) # Returns True
print(myUniqueList) # ['pizza', 'burger']
print(myLeftovers) # ['pizza']
