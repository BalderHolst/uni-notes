from readLines import *

path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/Medea - Tekst.md'

lines = read_lines(path)

for n in range(len(lines)):
	line = lines[n]

	lines[n] = "$\\tab$" + line


write_lines(path,lines)