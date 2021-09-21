from readLines import *

path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/I en Landsbykirke (1837).md'

lines = read_lines(path)

def isValue(input):
	try:
		int(input)
		return(True)

	except ValueError:
		return(False)


for n in range(len(lines)):
	line = lines[n]

	if(line.find('.') >= 0):
		lines[n] = '\t' + line
	elif(line.find("NOTER") >= 0):
		break

		

write_lines(path,lines)