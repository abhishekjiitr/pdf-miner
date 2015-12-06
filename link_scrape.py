from bs4 import BeautifulSoup
import re, socket, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
from urllib.parse import urlparse
from urllib.parse import urljoin
from collections import defaultdict
from time import time
import pickle, os
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse

f=open('out.txt','w+')
unvisited = []
unvisited_map = {}
visited = defaultdict(lambda: 0)
pdfs = []
local_ip = ""
def get_ip(url):
	#print(url)
	try:
		url = (socket.gethostbyname(urlparse(url).netloc)).split('.')
	except:
		pass
	return url[0] + "." + url[1] + "." + url[2]

def crawl():
	global local_ip, unvisited, visited, pdfs, unvisited_map, f
	website = unvisited.pop()
	print(website,"\n")
	f.write(website+"\n")
	visited[website] = 1
	req = urllib.request.Request(website)
	try:
		reponse = urllib.request.urlopen(req,timeout=5)
	except:
		print('Error 404 :Not Found')
		f.write('Error 404 :Not Found\n')
		return
	if 'text/html' in reponse.getheader('Content-Type'):
		try:
			page = reponse.read()
		except:
			return
	else:
		return
	soup = BeautifulSoup(page, 'html.parser')
	for link in soup.find_all('a'):
		path = link.get('href')
		if path == None:
			return
		if "http" == path[:4]:
			if "#" in path:
				return
			abs_link = path
		else:
			abs_link = urljoin(website, path)
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
		stri=("%d PDFs found, %d links scanned, %d links still left" % (len(pdfs), scanned, len(unvisited)))
		print(stri)
		stri=stri+"\n"
		f.write(stri)
	return pdfs

#get_links("http://www.iitr.ac.in/")
#print(get_links(url))
def get_pdf_links():
	global f
	grand_list = []
	filename = "final_domains.txt"
	data = open(filename, "r")
	directory = "pickled_links"
	for line in data.readlines():
		line = line[:len(line)-1]
		time1 = time()
		pdf_list = get_links(line)
		grand_list.append(pdf_list)
		time2 = time()
		diff = int(time2 - time1)
		#print(("%s website completed, %d time taken: %d, PDFs found: %d"%(line, diff, len(pdf_list))))
		line = urlparse(line).netloc.split(".")[1]+".p"
		if not os.path.exists(directory):
			os.makedirs(directory)
		dir_path = os.path.join(directory,line)
		print(dir_path)
		f.write(dir_path)
		pick_file = open(dir_path, "wb")
		pickle.dump(pdf_list, pick_file)
		pick_file.close()
	f.close()
	data.close()
	dir_path = os.path.join(directory,"grand_list.p")
	pickle_file = open(dir_path, "wb")
	pickle.dump(grand_list, pickle_file)
	pickle_file.close()

get_pdf_links()
