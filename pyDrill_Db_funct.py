# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Change the UI for working with the script used in a previous drill
#               (see pyDrill_scripting.py) to do file transfer by date and work with a db.

# Do necessary imports
import shutil
import os
import datetime as dt

def copyFile(src, dst):
    # sets current time to a variable
    now = dt.datetime.now()
    # sets the time 24 hours ago to a variable
    ago = now-dt.timedelta(minutes=1440)

    # looks in the source folder which was passed in
    for file in os.listdir(src):
         # creates new variable with the full path name to the file
         full_path = os.path.join(src, file)
         # sets time stamp to each file to the mtime variable
         st = os.stat(full_path)
         mtime = dt.datetime.fromtimestamp(st.st_mtime)
         # checks to see which files have been edited in the last day
         if mtime > ago:
             # checks to make sure only .txt files are being copied
             if file.lower().endswith(('.txt')):    
                 shutil.copy(full_path, dst)
                 print('%s modified %s'%(src +file, mtime))

copyFile("C:\Users\Dunning\Desktop\A", "C:\Users\Dunning\Desktop\B")
