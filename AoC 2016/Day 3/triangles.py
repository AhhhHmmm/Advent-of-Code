npossible = 0

with open('dimensions.txt') as f:
	for line in f:
		dims = line.split()
		dims = [int(dims[0].strip()),int(dims[1].strip()), int(dims[2].strip())]
		dims.sort()
		if dims[0] + dims[1] > dims[2]:
			npossible += 1

print(npossible)