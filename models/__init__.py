#!/usr/bin/python3
import sys
import os

dir = os.getcwd()
folder = 'engine'
_path = os.path.join(dir, folder)
sys.path.append(_path)

from engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
x = 4