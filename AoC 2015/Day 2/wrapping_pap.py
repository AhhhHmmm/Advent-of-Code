total_pap = 0

with open('gift_dimensions.txt') as f:
	for line in f:
		dim = line.split('x')
		surf_area = 2*int(dim[0])*int(dim[1]) + 2*int(dim[1])*int(dim[2]) + 2*int(dim[0])*int(dim[2])
		minim = min([int(dim[1])*int(dim[2]),int(dim[0])*int(dim[1]),int(dim[0])*int(dim[2])])
		print(surf_area + minim)
		total_pap += (surf_area + minim)

print(total_pap)
			
