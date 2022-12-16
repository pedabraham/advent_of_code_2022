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
    n = 1
    sum_orders = 0
    for i in range(0,n_lists,2):
        list_1 = lists[i]
        list_2 = lists[i+1]
        order = compare_lists(list_1,list_2)
        if order == 'right_order':
            sum_orders += n
        n += 1
    return sum_orders

def get_order(element,lists):
    n_lists = len(lists)
    wrongs = 0
    for i in range(n_lists):
        list_1 = lists[i]
        order = compare_lists(element,list_1)
        if order == 'worng_order':
            wrongs += 1
    return wrongs + 1


def compare_value(left,right):
    if isinstance(left,int) and isinstance(right, int):
        order = compare_ints(left,right)
        return order
    if isinstance(left,list) and isinstance(right, list):
        order = compare_lists(left,right)
        return order
    else:
        if isinstance(left,int):
            left = [left]
        if isinstance(right,int):
            right = [right]
        order = compare_lists(left,right)
        return order

def compare_lists(left,right):
    len_left = len(left)
    len_right = len(right)
    min_len = 0
    if len_left > len_right:
        min_len = len_right
    elif len_left < len_right:
        min_len = len_left
    else:
        min_len = len_right
    for i in range(min_len):
        order = compare_value(left[i],right[i])
        if order == 'unknown_order':
            continue
        else:
            return order
    if len_left < len_right:
        return 'right_order'
    elif len_left > len_right:
        return 'worng_order'
    return 'unknown_order'

def compare_ints(left,right):
    if left < right:
        return 'right_order'
    elif left > right:
        return 'worng_order'
    else:
        return 'unknown_order'

    
test_input = [
    '[1,1,3,1,1]',
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
sum_orders = process_lists(set_list)
print(sum_orders)


input_lists = None
with open('input_13.txt','r') as file:
    input_lists = file.readlines()

set_list = read_lists(input_lists)
sum_orders = process_lists(set_list)
print(sum_orders)

print(get_order([[2]],set_list+[[6]]))
print(get_order([[6]],set_list+[[2]]))
