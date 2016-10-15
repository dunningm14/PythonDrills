# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Write your own version of the sorted() method in Python. This method should take
#               a list as an argument and return a list that is sorted in ascending order. Call your
#               method passing in the following lists as an argument and print each sorted list into
#               the shell. This should be an algorithm you write, do not use the .sort() or the sorted()
#               methods in your method

# First list
rawList = [67, 45, 2, 13, 1, 998]
sortedList = []

while rawList:
    minimum = rawList[0]  
    for x in rawList: 
        if x < minimum:
            minimum = x
    sortedList.append(minimum)
    rawList.remove(minimum)    

print sortedList

# Second list
rawList = [89, 23, 33, 45, 10, 12, 45, 45, 45]
sortedList = []

while rawList:
    minimum = rawList[0]  
    for x in rawList: 
        if x < minimum:
            minimum = x
    sortedList.append(minimum)
    rawList.remove(minimum)    

print sortedList
