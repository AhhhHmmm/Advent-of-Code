import numpy as np
import re

size = 1000
light_array = np.zeros([size,size],dtype=int)

def trim_extra(line):
	return(re.findall(r'\d+',line))

def nextStep(array, line):
	if 'turn on' in line:
		num_info = trim_extra(line)
		for row_num in range(int(num_info[0]),int(num_info[2])+1):
			for col_num in range(int(num_info[1]),int(num_info[3])+1):
				array[row_num][col_num] += 1
	elif 'turn off' in line:
		num_info = trim_extra(line)
		for row_num in range(int(num_info[0]),int(num_info[2])+1):
			for col_num in range(int(num_info[1]),int(num_info[3])+1):
				if array[row_num][col_num] != 0:
					array[row_num][col_num] -= 1
	elif 'toggle' in line:
		num_info = trim_extra(line)
		for row_num in range(int(num_info[0]),int(num_info[2])+1):
			for col_num in range(int(num_info[1]),int(num_info[3])+1):
				array[row_num][col_num] += 2
	return(array)

def find_sum_array(array):
	sum = 0
	for row_num in range(array.shape[0]):
		for col_num in range(array.shape[1]):
			sum += array[row_num][col_num]
	return(sum)

with open('light_data.txt') as f:
	for line in f:
		light_array = nextStep(light_array, line)


#ah = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(find_sum_array(light_array))
#print(light_array)