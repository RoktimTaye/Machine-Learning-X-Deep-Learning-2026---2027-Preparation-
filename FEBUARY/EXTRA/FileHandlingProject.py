from pathlib import Path
import os

def readfilefolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
        
def createfile():
    try:
        readfilefolder()
        name = input("Please tell your file name :-")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
                
                print("FILE CREATED SUCESSFULLY")
        else:
            print("THIS FILE ALREADY EXISTS")
    except Exception as err:
        print(f"An error occured as {err}")
        
def readfile():
    try:
        readfilefolder()
        name = input("Which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print({"Readed Sucessfully"})
        else:
            print("The file dosen't exists")
    except Exception as err:
        print(f"An error has occured as {err}")
        
def updatefile():
    try:
        readfilefolder()
        name = input("Tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")
            
            res = int(input("Tell your response:- "))
            
            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
                
            if res == 2:
                with open(p,"w") as fs:
                    data = input("Tell what you want to append :- ")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error has occured as {err}")

def deletefile():
    try:
        readfilefolder()
        name = input("Which file you want to delete :-")
        p = Path(name)
        
        if p.exists() and p.is_file():
            os.remove(name)
            
            print("File removed Sucessfully")
            
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error has occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createfile()
    
if check == 2:
    readfile()
    
if check == 3:
    updatefile()
    
if check == 4:
    deletefile()