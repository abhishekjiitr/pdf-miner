import pickle, os
from urlparse import urlparse

def get_pdf_links():
    filename = "final_domains.txt"
    data = open(filename, "r")
    directory = "pickled_links"

    for line in data.readlines():
        line = urlparse(line).netloc.split(".")[1]+".p"
        pdf_list = ["pdf1", "pdf2"]
        if not os.path.exists(directory):
            os.makedirs(directory)
        print("############")
        dir_path = os.path.join(directory,line)
        print(dir_path)
        pick_file = open(dir_path, "wb")
        pickle.dump(pdf_list, pick_file)
        pick_file.close()
    data.close()

get_pdf_links()
