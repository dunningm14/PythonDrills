# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a script to automate the task of copying files to a specific location (folder B)
#               from their source (folder A) if the files have been created/edited within the past 24
#               hours.

# Do necessary imports
import shutil
import os

# sets folder source to move files from
for root, dirs, files in os.walk(r'C:\Users\Dunning\Desktop\A'):
    for ckfile in files:
        for root2, dirs2, files2 in os.walk(r'C:\Users\Dunning\Desktop\B'):
            # checks to make sure files haven't already been moved
            if ckfile not in files2:
                    # Tells you which files have been moved
                    print"Moving "+ckfile+" to back-up folder."
                    copyf = os.path.join(root,ckfile)
                    shutil.move(copyf, r'C:\Users\Dunning\Desktop\B')    
            else:
                # lets user know which files are already in the new folder
                print "This file: "+ckfile+" has already been copied"
