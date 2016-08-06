import link_scrape as ls
import down,xml_convertor
import curse,os,shutil
import NameExtractor ,EmailToNameMapping
import automata as auto 
from configuration import DOMAIN_LINK_FILE_LOCATION, PDF_DOWNLOAD_DIRECTORY
'''
The file FinalDomains.txt contains the urls of domains from which links of 
journals and research papers can be downloaded by recursive crawling.
'''
f=open(DOMAIN_LINK_FILE_LOCATION, 'r+')

'''
x is the list of all the domains in FinalDomains.txt 
'''
x=f.readlines()

#index variable counts the number of domain urls that have been traversed 
index = 0

'''
Iterate over each domain URL in the list x 
'''
for line in x:

    #Recursively crawl the given domain and collect the links of all the pdfs
    '''
    The list list_of_pdfs_from_ls stores the links 
    of all the pdfs under given domain
    '''
    list_of_pdfs_from_ls = ls.get_links(line.strip())

    #Iterate over each pdf in the list_of_pdfs_from_ls
    for i in range(len(list_of_pdfs_from_ls)):

        '''
        The pdf will be downloaded in the appropriate directory
        as specified in the down.py file
        '''
        #Try to download the pdf
        try:
            down.download_pdfs(list_of_pdfs_from_ls,i)
        #Skip if some exception occurs
        except Exception as e:
            print((str(e)))
            continue
    '''
    The function xml_convertor.recurse(directory)
    recurses the given directory and creates an xml 
    copy of every pdf found in the directory.
    These xml files are further used for extracting 
    names and emails based on regular expressions and 
    location of text in the pdfs as indicated in xml files.
    '''
    xml_convertor.recurse(PDF_DOWNLOAD_DIRECTORY)

    '''
    The function curse.recurse2(directory) gets all the work done 
    by processing the xml files to extract the names and emails 
    and delegating the task of mapping them to other functions .
    After getting the mapping ,it calls another function to populate
    the database specified in the curse.py 
    '''
    curse.recurse2(PDF_DOWNLOAD_DIRECTORY)

   
    #Increment the index if the task is successfully done for given domain
    index += 1

    i=0 #Utility suffix integer to resolve name clashes while moving files

    ''' 
    After processing the pdfs move them to another directory
    to make the download directory empty.
    '''
    auto.moving()
    
    print(str(index)+" domains have been processed.")

f.close()
