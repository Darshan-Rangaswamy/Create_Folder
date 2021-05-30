import os,sys
#Name of the first level folder
val = input ("Enter the Parent folder:")
#confirmation if the name is correct
print (val)
#change accoring to your preference
path = ("C:\\Users\\darshanr\\Documents\\PythonTesting\\Testfolder\\"+str(val))
#complete path of where the folder will be created
print ("Folder Created at:",path)
#enter if the path does not exist
if not os.path.exists(path):	
	#create folder at the specified path
	os.mkdir(path)
	print("The current working directory is %s" % path)
	try:
		#open txt with folder names
		with open("Folder_Names.txt", 'r') as x:
			for line in x:
				#strip and replace all unwanted symbols
				line = line.strip('\n')
				line = line.replace(' ','_')
				line = line.replace(',','_')
				line = line.replace(':','_')
				#adding folder name to the existing path
				path_new = (path+"\\"+str(line))
				print (path_new)
				#create subfolder in the path provided by er
				os.mkdir(str(path_new))
				path_new = path
		x.close()
	except OSError as e:
		print(e)
		print("TC Directory not created")
else:
	print ("Path exists, choose another path")