def read_lists(input):
    lists_list = list()
    for line in input:
        line = line.strip()
        if not line:
            continue
        list_stack = list()
        final_list = list()
        top_list = final_list
        for car in line:
            if car == '[':
                new_list = list()
                top_list.append(new_list)
                top_list = new_list
                list_stack.append(new_list)
            elif car == ']':
                list_stack.pop()
                if list_stack:
                    top_list = list_stack[-1]
            elif car == ',':
                continue
            else:
                number = int(car)
                top_list.append(number)
        lists_list.append(final_list)
    return lists_list

test_input = [
    '[[1],[2,3,4]]'
]

set_list = read_lists(test_input)
print(set_list)

print(1)