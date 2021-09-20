from readLines import *

path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/Medea - Tekst.md'

lines = read_lines(path)

def isValue(input):
	try:
		int(input)
		return(True)

	except ValueError:
		return(False)


for n in range(len(lines)):
	line = lines[n]

	if(line.find("Side") >= 0):

		new_line = "\n---\n" + line

		print(new_line)

		lines[n] = new_line 

write_lines(path,lines)