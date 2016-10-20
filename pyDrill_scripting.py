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
from os import path
import datetime
from datetime import date, time, timedelta

# set the location for source and destination folders and define the source and destination paths
archived_ctr = 0
ready_to_archive_ctr = 0
src_path = 'C:\Users\Dunning\Desktop\A'
dst_path = 'C:\Users\Dunning\Desktop\B'


def sourcePath(path):
  global src_path
  if os.path.exists(path):
    src_path = path
  else: return False


def destinationPath(path):
  global dst_path
  if os.path.exists(path):
    dst_path = path
  else: return False


def fileChanged(fname):


# retrieve the time when the file was changed
  file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))
  


# calculate the difference in time between when the file was changed and today
  td = datetime.datetime.now() - file_m_time
  

# set to archive if the changes were made in the past 24 hours
  if td.days == 0:
    global ready_to_archive_ctr
    ready_to_archive_ctr = ready_to_archive_ctr + 1
    return True
  else: return False
  


def MainLoop():

  global archived_ctr
  global src_path
  global dst_path

  for fname in os.listdir(src_path):

    src_fname = '%s\%s' % (src_path, fname)
        
    if fileChanged(src_fname):    
      dst_fname = '%s\%s' % (dst_path, fname)
     
      try:
        shutil.copy2(src_fname, dst_path)
        archived_ctr = archived_ctr + 1
      except IOError as e:
        print 'could not open the file: %s ' % e

  
def PrintResults():
  global ready_to_archive_ctr
  global archived_ctr
   
  print '***   Files Archived Today, %s   ***' % datetime.datetime.now()
  print '%d Ready to transfer ' % ready_to_archive_ctr
  print '%d transferred' % archived_ctr


def GetNumberFilesArchived():
  global archived_ctr
  return archived_ctr


if __name__ == "__main__":

  MainLoop()
  PrintResults()
