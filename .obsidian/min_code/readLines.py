def read_lines(path):	
	with open(path,"r") as f: 
		lines = f.readlines()
	return(lines)


def write_lines(path,lines):	
	with open(path,"w") as f: 
		f.writelines(lines)

if(__name__ == "__main__"):

	path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/Medea - Tekst.md'
	
	print(read_lines(path))
	
