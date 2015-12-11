import os
for root, dirs, files in os.walk(".", topdown=False):
	dictionary=dict()
	for name in files:
		path = (os.path.join(os.getcwd(), name))
		if path[-4:] == '.pdf':
			dictionary.append(os.path.join(os.getcwd(),root,'\b',name))
