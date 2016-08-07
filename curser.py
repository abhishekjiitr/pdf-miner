import os
import requests, time, csv, ast, sys, MySQLdb, os
import out1_pro,os
import EditDistance

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
add_record = "INSERT INTO nameemail (email, name, info, website) VALUES (%s, %s, %s, %s)"

def fire(name="", email="", info="", site=''):
    global add_record, cursor, cnx
    data_record = (email, name, info, site)
    cursor.execute(add_record, data_record )
    cnx.commit()

folders = []
i = 0
def recurse(folder):
    global i, folders
    for root, subdirs, files in os.walk(folder):
        i += 1
        if i ==1:
            folders = subdirs

def recursion(path2, folder):
    for root, subdirs, files in os.walk(path2):
        for filename in  files:
            if filename[-4:] == ".xml":
                path = os.path.join(root, filename)
                text,emails = out1_pro.callMe(path)
                if text != None:
                    w = EditDistance.textToMapping(text,emails)
                    for item in w:
                        # print(item, w[item],filename[:-4], folder)
                        try:
                            fire(w[item], item, filename[:-4], folder)
                        except Exception as e:
                            print("Exception in database updation " + str(e))
     


def recurse2(path):
    global folders
    recurse(path)
    for folder in folders:
        path2 = os.path.join(path, folder)
        recursion(path2, folder)
# recurse2(os.getcwd())
