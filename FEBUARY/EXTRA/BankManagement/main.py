from pathlib import Path
import os

def readfilefolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"{i+1} : {items}")