from bs4 import BeautifulSoup
import re, socket, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
from urllib.parse import urlparse
from urllib.parse import urljoin
from collections import defaultdict
from time import time
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse

unvisited = []
unvisited_map = {}
visited = defaultdict(lambda: 0)
pdfs = []
local_ip = ""
def get_ip(url):
    url = (socket.gethostbyname(urlparse(url).netloc)).split('.')
    return url[0] + "." + url[1] + "." + url[2]

def crawl():
    global local_ip, unvisited, visited, pdfs, unvisited_map
    website = unvisited.pop()
    visited[website] = 1
    req = urllib.request.Request(website)
    try:
        reponse = urllib.request.urlopen(req,timeout=5)
    except:
        print('Error 404 :Not Found')
        return
    if 'text/html' in reponse.getheader('Content-Type'):
        page = reponse.read()
    else:
        return
    soup = BeautifulSoup(page, 'html.parser')
    print(website) # for testing
    for link in soup.find_all('a'):
        path = link.get('href')
        if path == None:
            return
        if "http" == path[:4]:
            if "#" in path:
                return
            abs_link = urljoin(website, path)
        else:
            abs_link = link.get('href')
        if ( visited[abs_link] == 0 ):
            if abs_link[-4:] == ".pdf":
                visited[abs_link] = 1
                pdfs.append(abs_link)
            else:
                try:
                    ip = get_ip(abs_link)
                    if (ip == local_ip) and (abs_link not in unvisited_map):
                        unvisited.append(abs_link)
                        unvisited_map[abs_link] = 1
                except:
                    pass

def get_links(start_url):
    global unvisited, pdfs, unvisited_map, local_ip
    local_ip = get_ip(start_url)
    unvisited = []
    unvisited.append(start_url)
    unvisited_map[start_url] = 1
    scanned = 0
    while ( len(unvisited) > 0 ):
        crawl()
        scanned += 1
        print(("%d PDFs found, %d links scanned, %d links still left" % (len(pdfs), scanned, len(unvisited))))
    return pdfs

if __name__ == '__main__':
    dataFile = open(fileName,'r')
    for line in dataFile.readlines():
        pdf_list = get_links(line)