import numpy as np
import matplotlib.pyplot as plt
import re

little_screen = np.full((6,50),20)

def rectangle_on(screen, input_data,count):
	input_row = input_data[1]
	input_column = input_data[0]
	for row_num in range(0,input_row):
		for column_num in range(0,input_column):
			screen[row_num][column_num] = 70
	img = plt.imshow(screen,interpolation='nearest')
	img.set_cmap('GnBu')
	plt.axis('off')
	plt.savefig('./animation/animation%s.png'%count)
	count += 1
	return(screen,count)

def rotate_row(screen, input_data,count):
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
		img = plt.imshow(screen,interpolation='nearest')
		img.set_cmap('GnBu')
		plt.axis('off')
		plt.savefig('./animation/animation%s.png'%count)
		count += 1
	return(screen,count)

def rotate_col(screen, input_data,count):
	num_of_rotations = input_data[1]
	counter = 0
	temp_screen = np.transpose(screen)
	while counter < num_of_rotations:
		row_num = input_data[0]
		row = temp_screen[row_num]
		temp_row = []
		for val in range(len(row)):
			temp_row.append(row[(val-1)%len(row)])
		temp_screen[row_num] = temp_row
		counter += 1
		temp_screen = np.transpose(temp_screen)
		img = plt.imshow(screen,interpolation='nearest')
		img.set_cmap('GnBu')
		plt.axis('off')
		plt.savefig('./animation/animation%s.png'%count)
		count += 1
		temp_screen = np.transpose(temp_screen)
	temp_screen = np.transpose(temp_screen)
	return(temp_screen, count)
	
def parse_data(screen, file):
	count = 1
	temp_screen = screen
	with open(file) as f:
		for line in f:
			if 'rect' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen, count = rectangle_on(temp_screen,[int(values[0]),int(values[1])],count)
				print(count)
			elif 'rotate row' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen, count = rotate_row(temp_screen,[int(values[0]),int(values[1])],count)
			elif 'rotate column' in line:
				values = re.findall(r'\d+',line)
				#print(values)
				temp_screen, count = rotate_col(temp_screen,[int(values[0]),int(values[1])],count)
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
#with open('message.txt', 'w') as f:
#	end_matrix = parse_data(little_screen,'instructions.txt')
#	for row in end_matrix:
#		line_row = []
#		for col in row:
#			line_row.append(int(col))
#		print(line_row, file=f)