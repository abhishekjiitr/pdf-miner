import requests, time, csv, ast, sys, mysql.connector, os
import out1_pro,os
import EditDistance
config = {
'user': 'root',
'password': 'admin123',
'host': '127.0.0.1',
'port': '3306',
'database': 'bigdata',
'raise_on_warnings': True}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
add_record = ("INSERT INTO nameemail "
               "(email, name, info) "
               "VALUES (%s, %s, %s)")

def fire(name="", email="", info=""):
    global add_record, cursor, cnx
    data_record = (email, name, info)
    cursor.execute(add_record, data_record)
    cnx.commit()


def recurse(folder):
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:] == ".xml":
                path = os.path.join(root, filename)
                path = os.path.join(root, filename)
                text,emails = out1_pro.callMe(path)
                if text != None:
                    w = EditDistance.textToMapping(text,emails)
                    print "\n---from FINAL----"#, w#text,'\n\n ----  ',w
                    # if len(Emails)!=0:
                    #     print "$$$$$$",Emails
                    for item in w:
                        print item, w[item],filename[:-4]
                        fire(w[item], item, filename[:-4])
                    # print os.path.abspath(os.path.join(path, os.pardir))
                    # print os.pardir
                    print"-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx"



                #fire(email, name, info) # Fire query in DB
current = os.getcwd()
recurse(current)

cursor.close()
cnx.close()
