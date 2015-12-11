import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import os
from urllib.parse import urlparse
from PyPDF2 import PdfFileWriter,PdfFileReader
# dir = raw_input("Enter the directory where you want to save pdf")
list_of_pdfs = ['http://www.acas.org.uk/media/pdf/f/q/1111_Workplaces_and_Social_Networking-accessible-version-Apr-2012.pdf',
"http://www.psy.cmu.edu/~siegler/NCTM.pdf"]
def download_pdfs(list_of_pdfs,index):

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
	print(url)
	print(directory)

	os.chdir("/home/rishabh/git/pdf-miner/")
	if not os.path.exists(os.path.join(os.getcwd(),directory)):
		os.mkdir(directory)
	os.chdir(directory)
	file_name = url.split('/')[-1]
	if os.path.exists(os.path.join(os.getcwd(),file_name)) and not (os.path.getsize(os.path.join(os.getcwd(),file_name))):
		print("File exists and revoming: ")
		os.remove(os.path.join(os.getcwd(),file_name))
	if os.path.exists(os.path.join(os.getcwd(),file_name)):
		print("File exists :Skipping: ")
		#os.chdir(os.path.join(os.getcwd(),os.pardir))
		return

	try:
		u = urllib.request.urlopen(url,timeout = 100)
	except:
		print("Timeout \n")
		# os.chdir(os.path.join(os.getcwd(),os.pardir))
		return
	f = open(file_name,'wb+')
	# if hasattr(u,'getheaders'):
	# 	file_size = int(u.getheaders("Content-Length"))
	# elif hasattr(u,'getheader'):
	# 	file_size = int(u.getheader("Content-Length"))
	# elif hasattr(u.info(),'getheaders'):
	# 	file_size = int(u.info().getheaders("Content-Length")[0])
	# #else:
	# #	print("Header Error \n")
	# #	return
	# if file_size > 52428800:
	# 	print("File size>50 MB ")
	# 	#os.chdir(os.path.join(os.getcwd(),os.pardir))
	# 	return

	block_sz = 8192

	while True:
		buffers = u.read(block_sz)
		if not buffers:
			break
		# file_size_dl += len(buffers)
		f.write(buffers)

	#Code to discard all except the first page of the pdf
	# infile = PdfFileReader(f)
	# p = infile.getPage(0)
	# outfile = PdfFileWriter()
	# outfile.addPage(p)
	# with open(str(index)+file_name,'wb+') as f2:
	# 	outfile.write(f2)
	# f.close()
	# os.remove(os.getcwd()+os.sep+file_name)
