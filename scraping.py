from bs4 import BeautifulSoup
import re, socket
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
start_url = "http://www.iitr.ac.in/hi/departments/DPT/pages/Research+Publications.html"
unvisited = []
unvisited.append(start_url)
local = (urlparse(start_url).netloc)
# local = local.split(".")
# local = local[0]+"."+local[1]+"."+local[2]
visited = []
pdfs = []
def crawl():
    global unvisited
    global visited
    global local
    website = unvisited.pop()
    visited.append(website)
    #print(website)
    req = urllib.request.Request(website)
    try:
        response = urllib.request.urlopen(req)
    except:
        print("Not Found")
        return
    #print((response.getheader('Content-Type')))
    if  'text/html' in response.getheader('Content-Type'):
        page = response.read()
    else:
        return
    soup = BeautifulSoup(page, 'html.parser')
    #print((soup.prettify()))
    print(website)
    for link in soup.find_all('a'):        
        if "http" not in link:
            if "#" in link:
                return
            abs_link = urljoin(website, link.get("href"))
        else:
            abs_link = link.get('href')
        #print(abs_link)
        if abs_link not in visited:
            if re.search( '^.+\.pdf$', abs_link ):
                visited.append(abs_link)
                pdfs.append(abs_link)
            else:
                try:
                    ip = (urlparse(abs_link).netloc)
                    # ip = ip.split(".")
                    # ip = ip[0]+"."+ip[1]+"."+ip[2]
                    if (abs_link not in unvisited) and (ip == local):
                        unvisited.append(abs_link)
                except:
                    pass
i=0
while (len(unvisited)>0):
    # unvisited.sort()
    # for link in unvisited:
    #     print(link)
    # print((len(unvisited)))
    crawl()
    i=i+1
    print(len(pdfs), len(unvisited))
print("#############")
print(pdfs)
