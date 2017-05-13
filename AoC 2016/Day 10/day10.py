import re

bot_dictionary = {}

def parse_line(line):
    if line[0:5] == 'value':
        parse_value_line(line)
    else:
        parse_exchange_line(line)


def parse_value_line(line):
    bot_nums_find = re.compile(r'\d+')
    bot_nums = re.findall(bot_nums_find, line)
    bot_val = bot_nums[0]
    bot_number = bot_nums[1]
    if bot_dictionary.get(bot_number) == None:
        bot_dictionary[bot_number] = {bot_val}
    else:
        bot_dictionary[bot_number] = bot_dictionary[bot_number]| {bot_val}


def parse_exchange_line(line):
    bot_nums_find = re.compile(r'\d+')
    bot_nums = re.findall(bot_nums_find, line)
    bot_number = bot_nums[0]
    bot_gives_low = bot_nums[1]
    bot_gives_high = bot_nums[2]
    if bot_dictionary.get(bot_number) == None:
        pass
    elif len(bot_dictionary[bot_number]) != 2:
        pass
    else:
        list_nums = list(bot_dictionary[bot_number])
        holding_nums = [int(list_nums[0]),int(list_nums[1])]
        low_val = str(min(holding_nums))
        high_val = str(max(holding_nums))
        if bot_dictionary.get(bot_gives_low) == None:
            bot_dictionary[bot_gives_low] = {low_val}
        else:
            bot_dictionary[bot_gives_low] = bot_dictionary[bot_gives_low]| {low_val}
        if bot_dictionary.get(bot_gives_high) == None:
            bot_dictionary[bot_gives_high] = {high_val}
        else:
            bot_dictionary[bot_gives_high] = bot_dictionary[bot_gives_high]| {high_val}
        bot_dictionary[bot_number] = set()

def parse_all_lines(file):
    count = 0
    while {'17','61'} not in list(bot_dictionary.values()) and count < 100:
        with open(file) as f:
            for line in f:
                if {'17','61'} in list(bot_dictionary.values()):
                    return(list(bot_dictionary.keys())[list(bot_dictionary.values()).index({'17','61'})])
                else:
                    parse_line(line)
        count += 1
    return (list(bot_dictionary.keys())[list(bot_dictionary.values()).index({'17', '61'})])


print(parse_all_lines('data.txt'))