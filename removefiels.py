import os
import shutil
import time

def checkForOld(givenTime,oldValues):
      days=time.time()  
      diffTIme=days-givenTime                 # get difference in seconds need to convert in days
      diffdays=diffTIme/(24*60*60)            # convert difference of time in seconds into days
      if diffdays>oldValues:
        return True
      else: return False

path=input("enter the name of your directory")
oldValve=10
totalDirRemoved=0
totalFilesRemoved=0
if os.path.exists(path):
    for (root,dirs,files) in os.walk(path):
        
        for myDir in dirs:
          mypath=os.path.join(path,myDir)
          if os.path.exists(mypath):
            ctime= os.stat(mypath).st_ctime
            if checkForOld(ctime,oldValve):
                shutil.rmtree(mypath)
                totalDirRemoved=totalDirRemoved+1
        for myfiles in files:
          
          mypath=os.path.join(path,myfiles)
          if os.path.exists(mypath):
            ctime= os.stat(mypath).st_ctime
            if checkForOld(ctime,oldValve):
                os.remove(mypath)
                totalFilesRemoved=totalFilesRemoved+1

print('total files removed:-',totalFilesRemoved)
print('total directory removed:-',totalDirRemoved)
                



