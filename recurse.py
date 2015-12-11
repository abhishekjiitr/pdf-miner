import os
import EditDistance, NameExtractor
global_dict = {}
def recurse(folder):
    global global_dict
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:] == ".pdf":
                path = os.path.join(root, filename)
                print(path)
                temp_dict = EditDistance.nameemailpair(path)
                global_dict.update(temp_dict)
                for i in temp_dict:
                    print i
                    print temp_dict[i]
current = os.getcwd()
recurse(current)
for i in global_dict:
    print i+" "+global_dict[i]
