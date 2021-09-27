from readLines import *

path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/Brudstykker af Landsbydegnens Dagbog.md'

lines = read_lines(path)

i = 0

for n in range(len(lines)):
	line = lines[n]

	place = line.find("##### ")

	if(place >= 0):
		print(f"#### ({i})" + line[place + 5:])
		i += 1


	

		

write_lines(path[:-3] + " (edited).md",lines)