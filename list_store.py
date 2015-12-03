from urllib.parse import urlparse
import pickle
import os
from time import time


time = time()
hostname = urlparse("http://www.iitr.ac.in/hi/departments/DPT/pages/Research+Publications.html").netloc
abs_path = hostname+"/"+str(time)+".p"
if not os.path.exists(hostname):
    os.makedirs(hostname)
doc = open(abs_path, "wb")
print(hostname)
l = [1, 2, 3]
pickle.dump(l, doc)
doc.close()
l = pickle.load(open(abs_path, "rb"))
print(l)
