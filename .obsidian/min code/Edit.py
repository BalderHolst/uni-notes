from readLines import *

path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/I en Landsbykirke (1837).md'

lines = read_lines(path)

i = 0

for n in range(len(lines)):
	line = lines[n]

	place = line.find("##### ")

	if(place >= 0):
		print(f"#### ({i})" + line[place:])
		i += 1


	

		

write_lines(path,lines)