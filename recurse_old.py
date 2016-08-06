import os
import out1_pro
def recurse(folder):
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:] == ".xml":
                path = os.path.join(root, filename)
                out1_pro.callMe(path)
                print"\n\n-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
current = os.getcwd()
recurse(current)
