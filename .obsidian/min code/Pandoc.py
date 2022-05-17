import pypandoc
from glob import glob
import os.path



root_dir = "G:/My Drive/"

global target 
target = "C:/Users/balde/OneDrive/Documents/Balders Noter/Autoconverterede/"


def get_file_list(path):
    files = glob(path+"*.docx")
    return(files)

def get_dir_list(path):
	dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
	return(dirs)


def get_file_name_from_path(path):
	return(path.split('/')[-1].split('.')[0] + ".md")

def convertAndStore(in_path,out_path):
	pypandoc.convert_file(in_path, 'md', outputfile=out_path)


global files
files = []

def convertFiles(dir):
	print("leder efter .docs filer i " + dir)
	
	for f in get_file_list(dir):
		files.append(f)
	
	for d in get_dir_list(dir):
		convertFiles(dir + d + '/')




if __name__ == "__main__":

	#puts files in the files variable
	convertFiles(root_dir)

	for file in files:

		out_path = file


		file = file.replace('\\','/')
		
		fag = file[len(root_dir):].split('/')[1]
		
		navn = fag + " - " + get_file_name_from_path(file)

		new_file_name = target + navn

		print(new_file_name)
		convertAndStore(file,new_file_name)


		


		



	
