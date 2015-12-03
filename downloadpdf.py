import urllib
import urllib2
import os
from urlparse import urlparse
from PyPDF2 import PdfFileWriter,PdfFileReader
# dir = raw_input("Enter the directory where you want to save pdf")
list_of_pdfs = ['http://www.acas.org.uk/media/pdf/f/q/1111_Workplaces_and_Social_Networking-accessible-version-Apr-2012.pdf',
"http://www.psy.cmu.edu/~siegler/NCTM.pdf"]
def download_pdfs(list_of_pdfs,index):
	url = list_of_pdfs[index]
	directory = urlparse(url).netloc
	url.replace(' ','%20')
	directory.replace('~','til')
	print(directory)
	currendir = os.path.dirname(__file__)
	if not os.path.exists(os.path.join(os.getcwd(),directory)):
		os.mkdir(directory)
	os.chdir(directory)
	file_name = url.split('/')[-1]
	try:
		u = urllib2.urlopen(url)
	except:
		os.chdir(os.path.join(os.getcwd(),os.pardir))
		return
	f = open(file_name,'wb+')
	# meta = u.info()
	# file_size = int(meta.getheaders("Content-Length")[0])
	# print "Downloading : %s Bytes: %s" %(file_name,file_size)

	file_size_dl = 0
	block_sz = 8192

	while True:
		buffers = u.read(block_sz)
		if not buffers:
			break

		# file_size_dl += len(buffers)
		f.write(buffers)
		# status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
  #   	status = status + chr(8)*(len(status)+1)
  #   	print status,
  	infile = PdfFileReader(f)
  	p = infile.getPage(0)
  	outfile = PdfFileWriter()
  	outfile.addPage(p)
  	with open(str(index)+file_name,'wb+') as f2:
  		outfile.write(f2)
  	f.close()
  	os.remove(os.getcwd()+os.sep+file_name)

	os.chdir(os.path.join(os.getcwd(),os.pardir))
	