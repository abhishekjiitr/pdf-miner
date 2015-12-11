import os
def recurse(folder):
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:] == ".pdf":
                path = os.path.join(root, filename)
                os.system('pdftohtml -s -xml -i -c %s %s' % (path, path))
current = os.getcwd()
recurse(current)
