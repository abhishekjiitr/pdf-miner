import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import os
from urllib.parse import urlparse
from PyPDF2 import PdfFileWriter,PdfFileReader
from configuration import PDF_DOWNLOAD_DIRECTORY


def download_pdfs(list_of_pdfs,index):
	if not os.path.exists(PDF_DOWNLOAD_DIRECTORY):
		os.mkdir(PDF_DOWNLOAD_DIRECTORY)
	try:
		url = list_of_pdfs[index]
	except:
		print("Index out of range \n")
		return
	directory = urlparse(url).netloc
	url=url.replace(' ','%20')
	directory=directory.replace('~','til')
	if directory == '':
		return
	# print(url)
	# print(directory)

	os.chdir(PDF_DOWNLOAD_DIRECTORY)
	if not os.path.exists(os.path.join(os.getcwd(),directory)):
		os.mkdir(directory)
	os.chdir(directory)
	file_name = url.split('/')[-1]
	if os.path.exists(os.path.join(os.getcwd(),file_name)) and not (os.path.getsize(os.path.join(os.getcwd(),file_name))):
		print("File exists and revoming: ")
		os.remove(os.path.join(os.getcwd(),file_name))
	if os.path.exists(os.path.join(os.getcwd(),file_name)):
		print("File exists :Skipping: ")
		return

	try:
		u = urllib.request.urlopen(url,timeout = 100)
	except:
		print("Timeout \n")
		return
	f = open(file_name,'wb+')
	block_sz = 8192
	while True:
		buffers = u.read(block_sz)
		if not buffers:
			break
		f.write(buffers)
	f.close()

'''
	Function: download_pdfs

	Parameters:
		list_of_pdfs - a list of pdf links to download_pdfs
		index - starting index of link from where downloading will be started
		( Not used much, but used in case some error happened in downloading and some files have been downloaded )

	Returns:
		Nothing.
		Just saves the downloaded files in folder '/home/rishabh/downpdfs/'

	Note to User:
		None
'''