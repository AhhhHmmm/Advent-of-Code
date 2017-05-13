import numpy as np

npossible = 0

def dataTransform(file):
	data = np.empty((1,3))
	data_final = np.empty((1,3))
	with open(file) as f:
		for line in f:
			dims = line.split()
			temp_array = np.array([[int(dims[0].strip()),int(dims[1].strip()), int(dims[2].strip())]])
			data = np.vstack((data,temp_array))
	data = np.delete(data, (0), axis=0)
	data = data.transpose()
	for row_num in range(data.shape[0]):
		for group_num in range((data.shape[1])//3):
			data_final = np.vstack((data_final,data[row_num][group_num*3:group_num*3+3]))
			#print(data[row_num][group_num*3:group_num*3+3])
	data_final = np.delete(data_final, (0), axis=0)
	return(data_final)

data_final = dataTransform('dimensions.txt')


for row in data_final:
	row.sort()
	if row[0] + row[1] > row[2]:
		npossible += 1

print(npossible)

