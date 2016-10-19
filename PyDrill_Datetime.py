# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create code that will use the current time of the Portland HQ to find out the
#               time in the NYC & London branches, then compare that time with the branches
#               hours to see if they are open or closed.
#               Print out if each of the two branches are open or closed.


# Use Datetime Module
from datetime import datetime


# Set current time to Corpus Christi (my current location)
corpusTime = datetime.now()
corpusHour = corpusTime.hour


# Use the current time to calculate the Headquarters time (Portland Time)
portlandHour = corpusHour - 2


# Set Eastern time
newYorkHour = portlandHour + 3


# Set the eastern time hour code so that it does not exceed 24 hours
if newYorkHour >= 24:
    newYorkHour -= 24

    
# Check to see if the NYC branch is open or closed (open between 9:00 and 21:00)
if newYorkHour >= 9 and newYorkHour <= 21:
    print 'The New York Branch is open for business.'
else: print 'The New York Branch is closed.'


# Set London time
londonHour = portlandHour + 9


# Set the London time hour code so that it does not exceed 24 hours
if londonHour >= 24:
    londonHour -= 24


# Check to see if the London branch is open or closed (open between 9:00 and 21:00)
if londonHour >= 9 and londonHour <= 21:
    print 'The London Branch is open for business.'
else: print 'The London Branch is closed - Cheerio!'

