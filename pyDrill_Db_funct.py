# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a database function for the file transfer drill
#               (see pyDrill_scripting.py)

# Do Tkinter imports
from Tkinter import *
from tkFileDialog import *
import ttk
import tkMessageBox


# Do imports for the code
from datetime import timedelta
import os
import time
import shutil
import datetime as dt
import glob

# Do SQlite import for database
import sqlite3

## set up the database
def createDatabase():
    db = sqlite3.connect('test.db')
    print('Database opened')
    db.execute('DROP TABLE IF EXISTS fcRuns')
    db.execute('CREATE TABLE IF NOT EXISTS fcRuns (ID INTEGER PRIMARY KEY AUTOINCREMENT, fcTime TEXT)')
    print ('Table created.')
    db.commit()


class FileCheck:

    def __init__(self, master):

## Graphical User Interface

        # Frame for header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        
        # Set the folder to be checked daily
        self.dailyFolderName = StringVar()
        print (self.dailyFolderName)
        self.daily = (self.dailyFolderName.get())
        
        # Set the folder to recieve the copied files
        self.destFolderName = StringVar()
        print (self.destFolderName)
        self.dest = (self.destFolderName.get())

        self.fcTimestamp = StringVar()
        print (self.fcTimestamp)
        self.fcT = (self.fcTimestamp.get())
        
        # Title
        titleLabel = ttk.Label(self.frame_header, text = 'File Transfer Window ')
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')

        # Set up the frame for the labels and buttons
        self.frame_steps = ttk.Frame(master)
        self.frame_steps.pack()
      
        # Set up buttons   
        dailyButton = ttk.Button(self.frame_steps, text = 'Daily Folder', command = self.selectDailyFolder)
        dailyButton.grid(row = 1, column = 0, sticky = 'w')
        destButton = ttk.Button(self.frame_steps, text = 'Folder to Recieve Copies', command = self.selectDestFolder)
        destButton.grid(row = 4, column = 0, sticky = 'w')
        initiateButton = ttk.Button(self.frame_steps, text = 'Check Files', command = lambda: self.timeCompare(self.dailyFileCheck,self.destFileCheck))
        initiateButton.grid(row = 8, column = 0, sticky = 'w')
        
        # path labels
        self.frame_path = ttk.Frame(master)
        self.frame_path.pack()
        dailyPathLabel = ttk.Label(self.frame_steps, text = self.dailyFolderName, textvariable = self.dailyFolderName)
        dailyPathLabel.grid(row = 1, column = 2, rowspan = 1, sticky = 'W')
        dailyPathLabel.config(foreground = 'gray')
        destPathLabel = ttk.Label(self.frame_steps, text = self.destFolderName, textvariable = self.destFolderName)
        destPathLabel.grid(row = 4, column = 2, rowspan = 1, sticky = 'W')
        destPathLabel.config(foreground = 'gray')
   
        # label for the time stamp
        fcTimeTitleLabel = ttk.Label(self.frame_steps, text = 'The last file check was performed on:  ')
        fcTimeTitleLabel.grid(row = 7, column = 2, sticky = 'W' )
        fcTimestampLabel = ttk.Label(self.frame_steps, textvariable = self.fcTimestamp)
        fcTimestampLabel.grid(row = 8, column = 2, rowspan = 1, sticky = 'W')
        fcTimestampLabel.config(foreground = 'gray') 

    # Window used as a browser for the files in the 'daily' folder
    def selectDailyFolder(self):
        # open a window in the 'A' Folder
        self.dailyFileCheck = askdirectory(initialdir = "C:\Users\Dunning\Desktop\A", title = "Select the folder to be checked daily") 
        self.dailyFolderName.set(self.dailyFileCheck)
        print (self.dailyFileCheck)
        print (self.dailyFolderName.get())
        
    # Window used as a browser for the files in the folder to contain copies        
    def selectDestFolder(self):
        # open a window in the 'B' Folder
        self.destFileCheck = askdirectory(initialdir = "C:\Users\Dunning\Desktop\B", title = "Select folder to contain copies") 
        self.destFolderName.set(self.destFileCheck)
        print (self.destFileCheck)
        print (self.destFolderName.get())

        

# Script to automate the task of copying files to a specific location (folder B)
# from their source (folder A) if the files have been created/edited within the past 24
# hours.

    def timeCompare(self, dailyFileCheck, destFileCheck):
        # sets current time to a variable
        now = dt.datetime.now()
        # sets the time 24 hours ago to a variable
        ago = now-dt.timedelta(minutes=1440)

        # looks in the source folder which was passed in
        for file in os.listdir(dailyFileCheck):
             # creates new variable with the full path name to the file
             full_path = os.path.join(dailyFileCheck, file)
             # sets time stamp to each file to the mtime variable
             st = os.stat(full_path)
             mtime = dt.datetime.fromtimestamp(st.st_mtime)
             # checks to see which files have been edited in the last day
             if mtime > ago:
                 # checks to make sure only .txt files are being copied
                 if file.lower().endswith(('.txt')):    
                     shutil.copy(full_path, destFileCheck)
                     print('%s modified %s'%(dailyFileCheck +file, mtime)) 
             if mtime > ago:
                     print (full_path, "copied to: ", destFileCheck)
                     shutil.copy(full_path,destFileCheck) #copys file to destination
             else:
                     print (full_path, 'not copied')
        self.fileCheckdb() #inserts timestamp into db table                  

    #inserts timestamps to db
    def fileCheckdb(self):
        self.db = sqlite3.connect('test.db')
        print('Timestamp Database accessed.')
        self.db.execute("INSERT INTO fcRuns (fcTime) VALUES (datetime(CURRENT_TIMESTAMP, 'localtime'))")
        print('Timestamp recorded')
        self.db.commit()
        self.cursor = self.db.execute('SELECT fcTime FROM fcRuns ORDER BY ID DESC LIMIT 1')
        for row in self.cursor:
            print ('The last file check was performed on: ',row)
            self.fcClock = self.fcTimestamp.set(row)
            print ('adslkfjlsadf', row)
            
        self.db.close()
        print ('Database closed')
        
## Main Setup
                     
def main():
    
    root = Tk() #needed for tkinter
    root.wm_title("File Check") #sets the window title
    root.minsize(400, 280) #sets minimum size the window can be
    filecheck = FileCheck(root) #sets the class up with root from tkinter
    root.mainloop() #needed for tkinter


if __name__ == '__main__' :
    main() #runs the main function which runs the class and functions
    print ('Program run: Main')
