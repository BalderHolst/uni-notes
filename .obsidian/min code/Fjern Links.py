import os.path
from glob import glob

path = "C:/Users/balde/OneDrive/Documents/Balders Noter/Autoconverterede/"



def get_file_list(path):
    files = glob(path+"*.md")
    return(files)






files = get_file_list(path)



for file in files:
	try:
		with open(file,"r") as f: 
		   	text=f.readlines() 

		#print(file,text)

		#print()

		for n in range(len(text)):
			if(text[n].find("media") > 0):
				text[n] = "*der var et billede her engang*\n"
			if(text[n].find("[") > 0 and text[n].find("]") > 0 and text[n].find("/") > 0):
				text[n] = "\n"
			if(text[n].find("her var et link til en lokal fil") > 0):
				text[n] = "\n"

		with open(file,"w") as f: 
		   	f.writelines(text)

	except:
		print(file)

