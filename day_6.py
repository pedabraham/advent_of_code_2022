
def get_maker(message):
    length = int(len(message))
    #part 1 change 14 for 4
    for j in range(length-13):
        chars = set()
        for i in range(14):
            chars.add(message[j+i])
        if len(chars) == 14:
            return j + i+ 1
    return None


print(get_maker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))
print(get_maker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
