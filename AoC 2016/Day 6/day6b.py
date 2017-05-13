import numpy as np
import collections

direction_array = np.array([['','','','','','','','']])
code = ''

with open('directions.txt') as f:
	for line in f:
		direction_array
		line_list = list(line.strip())
		direction_array = np.vstack((direction_array, line_list))


direction_array = np.transpose(direction_array)

for row in direction_array:
	row_string = ''
	#print(row)
	for entry in row:
		row_string += entry
	row_string = row_string.strip()
	code += collections.Counter(row_string).most_common()[-1][0]
	
print(code)