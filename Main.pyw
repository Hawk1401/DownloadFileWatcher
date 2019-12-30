import time
import os
import shutil
from datetime import date

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def PlaceFileWithType(filePath, fileName):
    filename, file_extension = os.path.splitext(filePath)
    dir = FileTypes + "\\"+file_extension.replace(".","")
    if not os.path.exists(dir):
        os.mkdir(dir)
    shutil.copyfile(filePath, dir + "\\" + fileName)

def PlaceFileWithdate(filePath, fileName):
    today = date.today()
    dir = TimeSatampFiles + "\\" + str(today)
    if not os.path.exists(dir):
        os.mkdir(dir)
    shutil.copyfile(filePath, dir + "\\" + fileName)


downloadPath = get_download_path()
FileTypes = downloadPath + "\\FileTypes"
TimeSatampFiles = downloadPath + "\\Time"
try:
    if not os.path.exists(FileTypes):
        os.mkdir(FileTypes)
    if not os.path.exists(TimeSatampFiles):
        os.mkdir(TimeSatampFiles)
except:
    print("err");
while True:
    try:
        from os import listdir
        from os.path import isfile, join

        onlyfiles = [f for f in listdir(downloadPath) if isfile(join(downloadPath, f))]
        for file in onlyfiles:
            try:
                PlaceFileWithType(downloadPath +"\\"+ file,file)
                PlaceFileWithdate(downloadPath +"\\"+ file,file)
                os.remove(downloadPath +"\\"+ file)
            except:
                print("err")
        time.sleep(60) #sekunden
    except:
        print("err")

