import itertools

# write the file name for the file that contains input data
file = 'data.txt'

def create_dist_list(file):
	place_list = []
	dist_list = []
	with open(file, 'r') as f:
		for line in f:
			words = line.split()
			place1 = words[0]
			place2 = words[2]
			if place1 not in place_list:
				place_list.append(place1)
			if place2 not in place_list:
				place_list.append(place2)
			places = {place1,place2}
			dist = int(words[-1])
			dist_list.append([places,dist])
	return(place_list,dist_list)

def get_distance(perm, dist_list):
	distance = 0
	index = 0
	while index < (len(perm)-1):
		place_pair = {perm[index],perm[index+1]}
		for entry in dist_list:
			if entry[0] == place_pair:
				distance += entry[1]
		index += 1
	return(distance)

place_list, dist_list = create_dist_list(file)
# print(place_list)
# print(dist_list)

min_distance = 1000000000

all_perms = itertools.permutations(place_list)
for perm in all_perms:
	distance = get_distance(perm,dist_list)
	if distance < min_distance:
		print(perm)
		print(distance)
		min_distance = distance

# for entry in dist_list:
# 	if entry[0] == {'Dublin','London'}:
# 		print(entry[1])


