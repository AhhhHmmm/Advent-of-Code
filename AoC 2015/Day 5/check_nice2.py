#test_message = input("Test message: ")

def checkRepeatPair(message):
	num = 0
	check_repeat_pair = False
	while (num < len(message)-1 and check_repeat_pair == False):
		temp_string = message[:num] + ' ' + message[num+2:]
		if (message[num] + message[num+1]) in temp_string:
			check_repeat_pair = True
			num += 1
			break
		else:
			num += 1
	return(check_repeat_pair)

def checkSandwich(message):
	num = 0
	check_sandwich = False
	while (num < len(message)-2 and check_sandwich == False):
		if message[num] == message[num+2]:
			check_sandwich = True
			num += 1
			break
		else:
			num += 1
	return(check_sandwich)

def checkAll(message):
	if (checkRepeatPair(message) and checkSandwich(message)):
		return(True)
	else:
		return(False)

count_nice = 0

with open('santa_list.txt') as f:
	for line in f:
		count_nice += checkAll(line)
		#print(line + ' ' + str(checkRepeatPair(line)) + ', ' + str(checkSandwich(line)))

print(count_nice)


