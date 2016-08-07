import os
import requests, time, csv, ast, sys, pymysql, os
import out1_pro,os
import NameExtractor,EmailToNameMapping
from configuration import DATABASE_NAME, TABLE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST

cnx = pymysql.connect(host=DATABASE_HOST, user=DATABASE_USERNAME, passwd=DATABASE_PASSWORD, db=DATABASE_NAME)
cursor = cnx.cursor()

add_record = ("INSERT INTO "+TABLE_NAME+" (email, name, info, website) VALUES (%s, %s, %s, %s)")

def fire(name="", email="", info="", site=''):  
    global add_record, cursor, cnx
    data_record = (email, name, info, site)
    cursor.execute(add_record, data_record )
    cnx.commit()


folders = []
i = 0
# recurse is not used. only for testing purposes
def recurse(folder):
    global i, folders
    for root, subdirs, files in os.walk(folder):
        i += 1
        if i == 1:
            folders = subdirs


def recursion(path2, folder):
    for root, subdirs, files in os.walk(path2):
        for filename in  files:
            # print("this is the name of file")
            # print(filename)
            # print("\n\n")
            if filename[-4:] == ".xml":
                path = os.path.join(root, filename)
                text,emails = out1_pro.callMe(path)
                if text != None:
                    list_of_names = NameExtractor.textToNames(text)
                    w = EmailToNameMapping.emailToNameMapping(emails,list_of_names)
                    for item in w:
                        # print(item, w[item],filename[:-4], folder)
                        try:
                            fire(w[item], item, filename[:-4], folder)
                        except Exception as e:
                            print("Exception in database updation " + str(e))
                            continue
                    # print("-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx")


def recurse2(path):
    global folders
    recurse(path)
    for folder in folders:
        path2 = os.path.join(path, folder)
        recursion(path2, folder)

'''
 Function: fire
    Helper function to update database.

 Parameters: 
    name - Name of the person
    email - Email 
    info - Information
    site - website from where it was downloaded

 Returns:
    Nothing, just updates the Database.
    
 Note to User:
    Helper function to fire queries on DB.
'''
'''
 Function: recursion
    Helps recurse2 function that recursively visits all the xml files and calls other functions to extract name-email pairs and to saves
    rhem in a database.   
 Parameters: 
    path2 - the base path to the folder(name is base site), where all files of that website are saved.
    folder - specific folder(whose name is the base site from which the file is downloaded)

 Returns:
    Nothing
    
 Note to User:
    Don't call it directly. recurse2 calls it.
'''
'''
 Function: recurse2
    Main files which after extracting name-email pairs saves them in a database.

 Parameters: 
    path - the path to folder which contains the xml files(converted from pdf).

 Returns:
    Nothing
    
 Note to User:
    Run this function after you have got the .xml files converted from .pdf files. Put this file in the top level folder.
'''
