
start_string = 'abc'
number = 0
hash_of_string = str(hash(start_string+str(number)))

while hash_of_string[0:1] != '0':
	print(hash_of_string)
	number += 1
	hash_of_string = str(hash(start_string+str(number)))

print(start_string+str(number))