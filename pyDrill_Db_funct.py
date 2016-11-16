# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Create a database function for the file transfer drill
#               (see pyDrill_scripting.py)

# kinter imports
from Tkinter import *
import ttk

# Other Imports
import os
import shutil 
import datetime as dt
from tkFileDialog import *
import time

# Database imports
import sqlite3 
conn = sqlite3.connect('fileCheck.db') 
c = conn.cursor()

root = Tk()
root.title = ("File Transfer")
root.geometry('500x120+250+100')

#### Database Table and Functions ####

def create_table():
    conn = sqlite3.connect("file_check.db")           
    with conn:                                    
        c = conn.cursor()
        unix = time.time()
        datestamp = str(dt.datetime.fromtimestamp(unix).strftime('%d/%m/%Y'))
        c.execute("CREATE TABLE IF NOT EXISTS FileCheck(unix REAL, datestamp TEXT)")

        conn.commit()                             
    conn.close()
    first_run()                                                                         

def first_run():
    conn = sqlite3.connect("file_check.db")          
    with conn:                                       
        c = conn.cursor()
        c, count = count_records(c)              
        unix = time.time()
        datestamp = str(dt.datetime.fromtimestamp(unix).strftime('%d/%m/%Y'))
        if count < 1:                             
                          
            c.execute("""INSERT INTO FileCheck (unix, datestamp) VALUES (?,?)""",                      
                      (unix,datestamp,))            
            conn.commit()
    conn.close()
    show_date()

def show_date():
    conn = sqlite3.connect("file_check.db")           
    with conn:                                       
        c = conn.cursor()
        c.execute("""SELECT unix FROM FileCheck""")
        data = c.fetchone()[0]                        
        lastDate = float(data)                     
        readDate = dt.datetime.fromtimestamp(lastDate).strftime("%m/%d/%Y")
        var_date.set(readDate)                        
        conn.commit()
    conn.close()

def count_records(c):
    count = ""
    c.execute("""SELECT COUNT(*) FROM FileCheck""")    
    count = c.fetchone()[0]                          
    return c, count

#### Select directories and initiate ####

# Create Browse Buttons
def get_src():
                                          
    srcPath = askdirectory()     
    var_src.set(srcPath)

def get_dst():
                                          
    dstPath = askdirectory()
    var_dst.set(dstPath)


def file_trans():
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
                                            
    srcPath = var_src.get()
    dstPath = var_dst.get()
    for _file in os.listdir(srcPath):  
        if _file.endswith('.txt'):
            src = os.path.join(srcPath, _file)
            dst = os.path.join(dstPath, _file)
            st = os.stat(src)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print("( {} ) moved to: {}".format(_file,dstPath))
                shutil.move(src, dstPath)
        
                
#### GUI ####

mf = Frame(root)
mf.pack()

f1 = Frame(mf, width = 600, height = 250)
f1.pack(fill = X)
f2 = Frame(mf, width = 600, height = 250)
f2.pack()
f3 = Frame(mf, width = 600, height = 250)
f3.pack()


var_src = StringVar()
var_dst = StringVar()
var_date = StringVar()


# select origin folder
ttk.Label(f1, text = "Source Folder         : ").grid(row = 0, column = 0, sticky = 'w')
txt_src = Entry(f1, width = 40, textvariable = var_src)
txt_src.grid(row =0, column =1, padx =2, pady =2, sticky ='we', columnspan = 20)
Button1 = ttk.Button(f1, text = "Browse", command = get_src)
Button1.grid(row = 0, column = 22, sticky = 'e', padx = 8, pady = 4)

#select destination folder
ttk.Label(f2, text = "Destination Folder : ").grid(row = 1, column = 0, sticky = 'w')
txt_dst = Entry(f2, width = 40, textvariable = var_dst)
txt_dst.grid(row =1, column =1, padx =2, pady =2, sticky ='we', columnspan = 20)
Button2 = ttk.Button(f2, text = "Browse", command = get_dst)
Button2.grid(row = 1, column = 22, sticky = 'e', padx = 8, pady = 4)

#button for performing file transfer
Button3 = ttk.Button(f3, text= "Transfer Files", width =14, command= file_trans)
Button3.grid(row = 2, column = 22, sticky = 'e', padx = 10, pady = 10)

#label file transfer date
lbl_dt = ttk.Label(f3, text = "File Transfer Last Performed On:")
lbl_dt.grid(row = 2, column = 0, sticky = "w", padx = 8, pady = 4)
lbl_date = ttk.Label(f3, textvariable = var_date)
lbl_date.grid(row = 2, column = 1, sticky = "w", padx = 8, pady = 4)

create_table()


if __name__ == "__main__":
    dir_path = Label(root)
    dir_path.pack()
    first_run()
    root.mainloop()
