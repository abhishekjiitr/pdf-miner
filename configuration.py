import os

BASE_DIR = os.getcwd()


DOMAIN_LINK_FILE_LOCATION = os.path.join(BASE_DIR, 'finalDomains.txt')
PDF_DOWNLOAD_DIRECTORY = os.path.join(BASE_DIR, 'downloadedPdfs')
PDF_FILES_BACKUP_DIRECTORY = os.path.join(BASE_DIR, 'backup')
XML_FILES_DIRECTORY = os.path.join(BASE_DIR)
MINE_BASE_DIRECTORY = os.path.join(BASE_DIR, 'mine')
PDF_LINKS_FILE = os.path.join(MINE_BASE_DIRECTORY, 'pdf.txt')
OUTPUT_FILE_PATH = 'out.txt'

DATABASE_HOST = '127.0.0.1'
DATABASE_NAME = 'authors_db'
TABLE_NAME = 'nameemail'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'admin123'

