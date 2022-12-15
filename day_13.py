def read_lists(input_lists):
    lists_list = list()
    for line in input_lists:
        line = line.strip()
        if not line:
            continue
        list_stack = list()
        final_list = list()
        top_list = final_list
        last_c = None
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
                pass
            else:
                number = int(car)
                if last_c not in {'[',']',',',None}:
                    number = int(f'{last_c}{number}')
                    top_list.pop()
                top_list.append(number)
            last_c = car
        lists_list.append(final_list[0])
    return lists_list


def process_lists(lists):
    n_lists = len(lists)
    for i in range(0,n_lists,2):
        list_1 = n_lists[i]
        list_2 = n_lists[i+2]
        right_order = compare(list_1,list_2)

def compare(a,b):
    if type(a) == int and type(b) == int:
        pass
    return True

test_input = [
    '[[1],[2,3,48]]',
    '[1,1,5,1,1]',
    '',
    '[[1],[2,3,4]]',
    '[[1],4]',
    '',
    '[9]',
    '[[8,7,6]]',
    '',
    '[[4,4],4,4]',
    '[[4,4],4,4,4]',
    '',
    '[7,7,7,7]',
    '[7,7,7]',
    '',
    '[]',
    '[3]',
    '',
    '[[[]]]',
    '[[]]',
    '',
    '[1,[2,[3,[4,[5,6,7]]]],8,9]',
    '[1,[2,[3,[4,[5,6,0]]]],8,9]',
]

set_list = read_lists(test_input)
print(set_list)

print(1)