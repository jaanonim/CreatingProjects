import os
import sys

from data import PATH
from python import createPython
from web import createWeb

if __name__ == "__main__":
    try:
        type_ = str(sys.argv[2])
        name = str(sys.argv[3])
    except:
        type_ = str(input("Type (w - web, p - python): "))
        name = str(input("Name: "))

    type_ = type_.lower()
    if type_ == "w" or type_ == "web":
        try:
            path = str(sys.argv[1])
        except:
            path = str(input("Path: "))
        createWeb(path, name)
    else:
        path = PATH
        createPython(path, name)
