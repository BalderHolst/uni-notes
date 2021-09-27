from readLines import *
from Pandoc import *

end_path = 'C:/Users/balde/OneDrive/Documents/Balders Noter/J5 - Bevægelse på skråplan.md'
path = 'G:/My Drive/3. G/Fysik/Forsøg/J5 - Bevægelse på skråplan/J5 - Bevægelse på skråplan.docx'

convertAndStore(path,end_path)


#lines = read_lines(path)
#
#i = 0
#
#for n in range(len(lines)):
#	line = lines[n]
#
#	place = line.find("##### ")
#
#	if(place >= 0):
#		print(f"#### ({i})" + line[place + 5:])
#		i += 1


	

		

#write_lines(path[:-3] + " (edited).md",lines)