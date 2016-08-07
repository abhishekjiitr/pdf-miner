import os,shutil
from configuration import PDF_DOWNLOAD_DIRECTORY, PDF_FILES_BACKUP_DIRECTORY
'''
Function : move

Moves the content of one directory to another

Parameters :
    src - The source directory(Default values are given for the used linux system)
    des - The destination directory (Default values are given for use linux system)

Returns :
    Void
'''
def moving(src=PDF_DOWNLOAD_DIRECTORY,des=PDF_FILES_BACKUP_DIRECTORY):
    i=0
    for root, dirnames, filenames in os.walk(src):
        for direc in dirnames:
            try:
                #Utility module to cut and paste files from one directory to another
                shutil.move(os.path.join(root,direc), des)

            except OSError as e:
                print(str(e))
                #If error occurs due to clash of names,
        try:
            pass
            os.system("rm -r  " + src + "/*")
            # print(src)
        except OSError as e:
            print(str(e))
               