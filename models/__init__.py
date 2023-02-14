#!/usr/bin/python3
<<<<<<< HEAD
=======
import sys
import os

dir = os.getcwd()
folder = 'engine'
_path = os.path.join(dir, folder)
sys.path.append(_path)

>>>>>>> 85adc1edd3cad8c24d1583fe97042cc26c682d10
from engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
x = 4