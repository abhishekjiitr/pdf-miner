import os
def recurse(folder):
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:] == ".pdf":
                path = os.path.join(root, filename)
                # testing = 'pdftohtml -s -xml -i -c -q %s %s' % (path, path)
                # print (testing)
                os.system('pdftohtml -s -xml -i -c -q %s %s' % (path, path))
# current = os.getcwd()
# recurse(current)
'''
 Function: recurse
 	iterates over all files in current folder and recursively visits each folder in current folder and converts all 
 	.pdf files to .xml files

 Parameters: 
 	folder - the folder on which you want to run the Function

 Returns:
 	Nothing
 	
 Note to User:
 	Run this function after you have got the .pdf files. Put this file in the top level folder.
 	Then run this script. 
'''