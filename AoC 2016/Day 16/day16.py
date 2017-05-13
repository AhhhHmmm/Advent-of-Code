def step(input_string):
    mod_string = ''
    for char in input_string:
        new_char = (int(char) + 1)%2
        mod_string += str(new_char)
    mod_string = mod_string[::-1]
    new_string = input_string + '0' + mod_string
    return(new_string)

def make_dragon(input_string,max_length):
    length = len(input_string)
    temp_string = input_string
    while length < max_length:
        temp_string = step(temp_string)
        length = len(temp_string)
    return(temp_string[:max_length])

def check_sum(input_string):
    temp_string = input_string
    digits = len(temp_string)
    while digits % 2 == 0:
        index = 0
        new_string = ''
        while index < len(temp_string):
            if temp_string[index] == temp_string[index+1]:
                new_string += '1'
            else:
                new_string += '0'
            index += 2
        temp_string = new_string
        digits = len(temp_string)
    return(temp_string)

puzzle_input = '01111010110010011'
#max_length = 272
max_length = 35651584

#print(make_dragon(puzzle_input,max_length))
print(check_sum(make_dragon(puzzle_input,max_length)))