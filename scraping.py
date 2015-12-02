from bs4 import BeautifulSoup
import re, socket
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
start_url = "http://www.iitb.ac.in/"
unvisited = []
unvisited.append(start_url)
local = socket.gethostbyname(urlparse(start_url).netloc)
visited = []
pdfs = []
def crawl():
    global unvisited
    global visited
    global local
    website = unvisited.pop()
    visited.append(website)
    #-++779printlkpcc(website)
    req = urllib.request.Request(website)
    response = urllib.request.urlopen(req)
    print((response.getheader('Content-Type')))
    if  'text/html' in response.getheader('Content-Type'):
        page = response.read()
    else:
        return
    soup = BeautifulSoup(page, 'html.parser')
    #print((soup.prettify()))
    for link in soup.find_all('a'):        
        if "http" not in link:
            abs_link = urljoin(website, link.get("href"))
        else:
            abs_link = link.get('href')
        print(abs_link)
        if abs_link not in visited:
            if re.search( '^.+\.pdf$', abs_link ):
                visited.append(abs_link)
                pdfs.append(abs_link)
            else:
                if (abs_link not in unvisited) and (socket.gethostbyname(urlparse(abs_link).netloc) == local):
                    unvisited.append(abs_link)


while (len(unvisited) > 0):
    unvisited.sort()
    for link in unvisited:
        print(link)
    print((len(unvisited)))
    x = eval(input())
    crawl()
print("#############")
print(pdfs)
