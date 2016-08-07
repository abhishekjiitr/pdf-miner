# from nltk import metrics

'''
Function : editDistDP

Utility function that computes the editdistance
(Levenshtein distance) between two strings
The Levenshtein distance is a metric to measure difference 
between two sequences of characters

Parameters : 
	str1 - The first string 
	str2 - The second string 
	m - length of first string 
	n - length of second string 

Returns : 
	The editdistance between two strings of length m and n respectively

'''

def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]

'''
Function :edit_distance

Delegates the computation of Levenshtein distance to 
the function editDistDP

'''
def edit_distance(str1,str2):
	return editDistDP(str1,str2,len(str1),len(str2))

'''
Function : emailToNameMapping

For each email in the emailList:
	For each name in the nameList:
		Compute the editdistance of email and name 
		if the editdistance is minimum for selected email and name pair:
			given name is suitable candidate for selected email 

Parameters : 
	emailList - List of emails extracted from a given xml file 
	nameList - List of possible names extracted from the same xml file 

Returns :
	A dictionary consisting of email as keys corresponding mapped name as values

'''
def emailToNameMapping(emailList,nameList):
	dictOfEmails = dict()
	name = ''
	finalEmailNameMapping = dict()

	for j in range(len(emailList)):
		editdistance = 1000 #initialize the editdistance to a large value
		mindistance = 1000  #initialize minimum editdistance for a compound
							#name's(eg: Sharanpreet Singh Lobana) individual components(eg Singh)

		#Filter the email for computing the editDistance by removing the digits
		filteredEmail = emailList[j].split('@')[0]
		filteredEmail = ''.join([str(i) for i in filteredEmail if not i.isdigit()])
		# print(filteredEmail)

		for n in range(len(nameList)):
			if len(nameList[n].split())>1:  #if name consists of more than one component(eg Rahul Kashyap)
				subnames = nameList[n].split() #separate name into its components
				#Remove any dots from the subnames(eg [P.,Kumar] changes to [P,Kumar])
				subnames = [w.replace('.','') for w in subnames]

				for m in range(len(subnames)):
					if(len(subnames[m])>2): #Compute the edit distance only if the subname is not an abbrevation(eg: Dr)
						distance = edit_distance(filteredEmail.lower(),subnames[m].lower())
						if distance < mindistance:
							#If the editDistance found is less than the mindistance so far
							mindistance = distance #Update the mindistance for the subnames

				if mindistance < editdistance:
					# if the editdistance for given name is minimum among all the names compared so far
					editdistance = mindistance # Update the minimum editdistance
					name = nameList[n]  #Current best match is the given name

				combinedname = nameList[n].replace(' ','') #Check editdistance for the combinedname as well
				combinedname = combinedname.replace('.','')#Remove all the dots in the combinedname
				distance = edit_distance(filteredEmail.lower(),combinedname.lower())
				if distance < editdistance:
					editdistance = distance #if editDistance is less than current minimum
					name = nameList[n]      #Current best mapping

				#Hardcoding the initials matching for len(subnames)<=3
				if len(subnames) <=4 and len(subnames) >=2:
					booleanList = list()
					length = len(subnames)
					if length == 4:
						booleanList = [[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],\
						[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
					elif length == 3:
						booleanList = [[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
					else:
						booleanList = [[0,1],[1,0],[1,1]]
					for z in range(len(booleanList)):
						smallText =''
						smallList = booleanList[z]
						for y in range(length):
							if smallList[y] == 1:
								try:
								    smallText = smallText + subnames[y][0].lower()
								except Exception as e:
									print(str(e))
							else:
								smallText = smallText + subnames[y].lower()
						distance = edit_distance(filteredEmail.lower(),smallText)
						if distance < editdistance:
							editdistance = distance #if editDistance is less than current minimum
							name = nameList[n]
			#if name contains a single character
			else:
				distance = edit_distance(filteredEmail.lower(),nameList[n].lower())
				if distance < editdistance:
					editdistance = distance
					name = nameList[n] #Current best mapping

		try:
			finalEmailNameMapping[emailList[j]] = name #Update the mapping frequency corresponding to given name
		except Exception as e:
			print (str(e))

	#Return the dictionary of email and name mappings
	return finalEmailNameMapping
