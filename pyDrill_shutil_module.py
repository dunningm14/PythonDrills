# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a program to move files from Folder A to Folder B, and print out each file path
#               that was moved. Verify this by assuring that the moved file is no longer in Folder A
#               after the execution.
#
# This was tested on the following OS: Windows 10


# Do the necessary imports to access folders
import shutil
import os
from os import path

# Defining the main function
def main():

# Set the location of the list of files to folder A on the desktop    
    fileList = os.listdir('C:\Users\Dunning\Desktop\A')


# Set the source and location for the file transfer
    for fname in os.listdir('C:\Users\Dunning\Desktop\A') :
        src_fname = 'C:\Users\Dunning\Desktop\A\%s' % fname
        dst_fname = 'C:\Users\Dunning\Desktop\B\%s' % fname

# Create the printout for after the files are moved
        print 'Move file %s ' % (src_fname)
        print '  To the following location: %s ' % (dst_fname)

# Perform the move
        shutil.move(src_fname, dst_fname)



if __name__ == "__main__":
  main()
