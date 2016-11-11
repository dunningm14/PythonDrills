# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a UI for working with the script used in a previous drill
#               (see pyDrill_scripting.py)

# Do Tkinter imports
from tkinter import *
from tkinter import ttk as ttk, messagebox, filedialog

# Do imports for the code
from datetime import datetime, timedelta
import os
import time
import shutil
from glob import glob


class FileCheck:

    def __init__(self, master):

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
        
        # Title
        headerLabel = ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        titleLabel = ttk.Label(self.frame_header, text = 'File Transfer Drill ')
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
   


    # Window used as a browser for the files in the 'daily' folder
    def selectDailyFolder(self):
        # open a window in the 'A' Folder
        self.dailyFileCheck = filedialog.askdirectory(initialdir = "C:\Users\Dunning\Desktop\A", title = "Select the folder to be checked daily") 
        self.dailyFolderName.set(self.dailyFileCheck)
        print (self.dailyFileCheck)
        print (self.dailyFolderName.get())
        
# Window used as a browser for the files in the folder to contain copies        
    def selectDestFolder(self):
        # open a window in the 'B' Folder
        self.destFileCheck = filedialog.askdirectory(initialdir = "C:\Users\Dunning\Desktop\B", title = "Select folder to contain copies") 
        self.destFolderName.set(self.destFileCheck)
        print (self.destFileCheck)
        print (self.destFolderName.get())


# Script to automate the task of copying files to a specific location (folder B)
# from their source (folder A) if the files have been created/edited within the past 24
# hours.                    
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

def main():
    root = Tk() 
    root.wm_title("File Check")
    root.minsize(400, 280)
    filecheck = FileCheck(root) 
    root.mainloop()

if __name__ == '__main__' : main() 
