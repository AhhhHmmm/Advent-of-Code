total_rib = 0

with open('gift_dimensions.txt') as f:
	for line in f:
		dims = line.split('x')
		dim_nums = []
		for dim in dims:
			dim_nums.append(int(dim))
		vol = 1
		for num in dim_nums:
			vol *= num
		dim_nums.sort()
		per = 2*dim_nums[0]+2*dim_nums[1]
		total_rib += vol + per

print(total_rib)
			
