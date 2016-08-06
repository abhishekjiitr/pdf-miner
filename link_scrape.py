from bs4 import BeautifulSoup
import re, socket, urllib.request, urllib.parse, urllib.error, urllib.error, urllib.parse
from urllib.parse import urlparse
from urllib.parse import urljoin
from collections import defaultdict
from time import time
import pickle, os
from configuration import MINE_BASE_DIRECTORY, PDF_LINKS_FILE, OUTPUT_FILE_PATH

mine = MINE_BASE_DIRECTORY
if not os.path.exists(mine):
	os.makedirs(mine)

miner = open(PDF_LINKS_FILE, "w+")
f=open(OUTPUT_FILE_PATH ,'w+')
unvisited = []
unvisited_map = {}
visited = defaultdict(lambda: 0)
pdfs = []
local_ip = ""
numPDF = 0
numUnvisited = 0

def crawl():
	global local_ip, unvisited, visited, pdfs, unvisited_map, f, numPDF, numUnvisited
	website = unvisited.pop()
	numUnvisited -= 1
	print((website,"\n"))
	f.write(website+"\n")
	visited[website] = 1
	try:
		req = urllib.request.Request(website)
	except:
		return
	page = "xyz"
	if website[-4:] == ".pdf":
		pdfs.append(website)
		numPDF += 1
		return
	try:
		reponse = urllib.request.urlopen(req,timeout=5)
	except:
		print('Error 404 :Not Found')
		f.write('Error 404 :Not Found\n')
		return
	# print('The Content-Type of processing url is: '+str(reponse.getheader('Content-Type')))
	try:
		if 'text/pdf' in reponse.getheader('Content-Type') or 'application/pdf' in reponse.getheader('Content-Type') or 'application/x-pdf' in reponse.getheader('Content-Type'):
			pdfs.append(abs_link)
			numPDF += 1
			return
		if 'text/html' in reponse.getheader('Content-Type'):
			page = reponse.read()
		else:
			return
	except:
		print("Invalid Response")
		return
	soup = BeautifulSoup(page, 'html.parser')
	for link in soup.find_all('a'):
		path = link.get('href')
		classlink = link.get('class')
		idlink = link.get('id')
		if path == None or path=='' or path[0] == '#':
			return
		if '\n' in path or '\r' in path:
			path=path.replace('\n','')
			path=path.replace('\r','')
			print('New line or carriage return character found in path')
		if "http" == path[:4]:
			abs_link = path
		else:
			abs_link = urljoin(website, path)
		if ( visited[abs_link] == 0 ):
			if abs_link[-4:] == ".pdf":
				visited[abs_link] = 1
				pdfs.append(abs_link)
				numPDF += 1
			else:
				try:
					ip = (urlparse(abs_link).netloc)
					if (ip == local_ip) and (abs_link not in unvisited_map):
						unvisited.append(abs_link)
						unvisited_map[abs_link] = 1
						numUnvisited += 1
				except:
					pass

def get_links(start_url):
	global unvisited, pdfs, unvisited_map, local_ip, numPDF, numUnvisited, miner
	numUnvisited = 0
	local_ip = (urlparse(start_url).netloc)
	unvisited = []
	unvisited.append(start_url)
	numUnvisited += 1
	unvisited_map[start_url] = 1
	scanned = 0
	while ( numUnvisited > 0 ):
		crawl()
		if ( (numPDF != 0)  and numPDF % 100 == 0 ):
			for var in range(numPDF-100, numPDF):
				miner.write(pdfs[var]+"\n")
		scanned += 1
		stri=("%d PDFs found, %d links scanned, %d links still left" % (numPDF, scanned, numUnvisited))
		print(stri)
		stri=stri+"\n"
		f.write(stri)

	return pdfs
'''
	Function: get_links
		Does the job of getting the links of all pdf files found on a particular site provided, and also writes them in a file 
		named out.txt

	Parameters:
		start_url - url of the base site from which we want to extract pdf links

	Returns:
		list of all pdf links found on a specified website
	Uses:
		Function - crawl()
'''
'''
	Function: crawl
		This is the main recursive crawling function that helps the get_links function to get all pdf links.

	Parameters:
		No parameters.
		All variables are already set by script and get_links fucntion.
	
	Returns:
		Nothing
	
	Note to user:
		This function is a helper function called by get_links function. It is not intended to be invoked manually by user.
'''