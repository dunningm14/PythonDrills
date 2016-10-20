# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a UI for working with the script used in a previous drill
#               (see pyDrill_scripting.py)

import wx
import os
import datetime as dt
import shutil

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(300,250))

        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()

        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+P')

        #Create menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()

        #Add items to to the menu
        fileMenu.Append(wx.NewId(), "New File", "Create New")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Done")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        # View and select files that are to be moved every 24 hours
        directory = wx.DirSelector("Choose Folder")

        if not directory.strip():
            # Exit when the user quits
            self.exit()

        # View and select recieving folder
        directory = wx.DirSelector("Choose Recieving Folder")

        if not directory.strip():
            # Exit when the user quits
            self.exit()
        
        # Create the query box to run the script
        yesNoBox = wx.MessageDialog(None, 'Check for new files?',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        # Text box panel
        wx.TextCtrl(panel, pos=(3, 100), size=(150,50))

        # Text
        aweText = wx.StaticText(panel, -1, "Transfer Complete", (3,3))

        self.SetTitle('Hello')

        self.Show(True)

    def Quit(self, e):
        self.Close()
        
        
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

for root,dirs,files in os.walk('C:\Users\Dunning\Desktop\B'):

    for item in files:
        now = dt.datetime.now()
        yesterday = now - dt.timedelta(hours=24)
        path = os.path.join(root,item)
        st = os.stat(path)

    mod_time = dt.datetime.fromtimestamp(st.st_ctime)
    if mod_time < yesterday:
        shutil.move(os.path.join(root,item), 'C:\Users\Dunning\Desktop\A')
        print('Transfer successful')
    else:
        print('%s last modify: %s'%(path,mod_time))
