import os
from os import listdir
from os.path import isfile, join, abspath

from logging import exception
from os import scandir


# print("insert the requested path to open new file")
# Path= input()
folder_path=r'C:\Users\User\Documents\תכנות שנה ב\newFolder'
file_path = os.path.join(folder_path, 'my_file.txt')
def createFolder (Path):
 if not os.path.exists(Path):
  os.mkdir(Path)
  print("Directory " , Path , " Created ")
 else:
     print("Directory " , Path , " already exists")

def deleteFolder (Path):


    if not os.path.exists(Path) :
        print("file didnt found")
    else:
        if os.path.exists(Path):
            os.rmdir(Path)
            print("folder deleted")
        else:
          print("folder iswnt empty , you cant delete")

def createFile (Path):
    with open(Path, "w") as file:
        file.write("Hei, good to see you:)")
    with open(Path, "a") as file:
        file.write("additional text")

def DeleteFile (filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print("file deleted")
    else:
        exception("file didnt found")

def PrintListFiles (Path):
    onlyfiles = [f for f in listdir(Path) if isfile(join(Path, f))]
    print(onlyfiles)

def GetFolderPath (Folder):
    print (os.path.abspath(Folder))

createFolder(folder_path)
createFile(file_path)
PrintListFiles(folder_path)
DeleteFile(file_path)
deleteFolder(folder_path)

