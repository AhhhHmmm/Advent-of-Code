import numpy as np
import re

little_screen = np.zeros((6,50))

def rectangle_on(screen, input_data):
	input_row = input_data[1]
	input_column = input_data[0]
	for row_num in range(0,input_row):
		for column_num in range(0,input_column):
			screen[row_num][column_num] = 1
	return(screen)

def rotate_row(screen, input_data):
	num_of_rotations = input_data[1]
	counter = 0
	while counter < num_of_rotations:
		row_num = input_data[0]
		row = screen[row_num]
		temp_row = []
		for val in range(len(row)):
			temp_row.append(row[(val-1)%len(row)])
		screen[row_num] = temp_row
		counter += 1
	return(screen)

def rotate_col(screen, input_data):
	temp_screen = np.transpose(screen)
	rotate_row(temp_screen,input_data)
	temp_screen = np.transpose(temp_screen)
	return(temp_screen)
	
def parse_data(screen, file):
	temp_screen = screen
	with open(file) as f:
		for line in f:
			if 'rect' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen = rectangle_on(temp_screen,[int(values[0]),int(values[1])])
			elif 'rotate row' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen = rotate_row(temp_screen,[int(values[0]),int(values[1])])
			elif 'rotate column' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen = rotate_col(temp_screen,[int(values[0]),int(values[1])])
	return(temp_screen)

def sum_matrix(screen):
	temp_screen = screen
	sum = 0
	for row in temp_screen:
		for col in row:
			sum += col
	return(sum)

#Challenge 1
print(int(sum_matrix(parse_data(little_screen,'instructions.txt'))))

#Challenge 2
with open('message.txt', 'w') as f:
	end_matrix = parse_data(little_screen,'instructions.txt')
	for row in end_matrix:
		line_row = []
		for col in row:
			line_row.append(int(col))
		print(line_row, file=f)

