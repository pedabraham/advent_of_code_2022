def gat_dict(monkeys):
    look_up = dict()
    for monkey in monkeys:
        monkey= monkey.strip()
        data = monkey.split()
        monkey_id = data[0].strip(':')
        number = None
        part1 = None
        part2 = None
        sing = None
        if len(data) == 2:
            number = int(data[1])
        else:
            part1 = data[1]
            part2 = data[3]
            sing = data[2]

        look_up[monkey_id] = {
            'number' : number,
            'part1': part1,
            'part2': part2,
            'sing': sing,}
    return look_up

def get_number(key,look_up):
    data = look_up.get(key)
    number = data.get('number')
    if key == 'humn':
        return None
    if number:
        return number
    else:
        monkey_1 = data.get('part1')
        monkey_2 = data.get('part2')
        number_1 = get_number(monkey_1,look_up)
        number_2 = get_number(monkey_2,look_up)
        if not number_1 or not number_2:
            return None
        sign = data.get('sing')
        if sign == '+':
            number = number_1 + number_2
        elif sign == '-':
            number = number_1 - number_2
        elif sign == '*':
            number = number_1 * number_2
        elif sign == '/':
            number = number_1 / number_2
        data['number'] = number
        return number

def print_eq(look_up, key,eq_q,temp_q):
    top_op = temp_q[-1]
    data = look_up.get(key)
    number = data.get('number')
    if key == 'humn':
        #top_op.append('X')
        print('X')
    elif number:
        top_op.append(number)
        print(number)
    else:
        monkey_1 = data.get('part1')
        monkey_2 = data.get('part2')
        print('(')
        new_top = list()
        eq_q.append(new_top)
        temp_q.append(new_top)
        print_eq(look_up, monkey_1,eq_q,temp_q)
        sign = data.get('sing')
        top_op = temp_q[-1]
        top_op.append(sign)
        print(sign)
        print_eq(look_up, monkey_2,eq_q,temp_q)
        temp_q.pop()
        print(')')

        #if not number_1 or not number_2:
        #    return None
        #if sign == '+':
        #    number = number_1 + number_2
        #elif sign == '-':
        #    number = number_1 - number_2
        #elif sign == '*':
        #    number = number_1 * number_2
        #elif sign == '/':
        #    number = number_1 / number_2
        #data['number'] = number
        #return number
    return eq_q

def process_eq(eq_q,match):
    inverse_op = {
        '+':'-',
        '-':'+',
        '*':'/',
        '/':'*'
    }

    for operation in eq_q:
        part1 = operation[0]
        part2 = operation[1]
        if isinstance(part1,str):
            number_1 = part2
            number = part2
            sign = inverse_op.get(part1)
            number_2 = match
        else:
            sign = inverse_op.get(part2)
            if part2 in {'-','/'}:
                number_1 = part1
                number_2 = match
                sign = part2
            else:
                number_1 = match
                number_2 = part1
            number = part1
        
        
        if sign == '+':
            match = number_1 + number_2
        elif sign == '-':
            match = number_1 - number_2
        elif sign == '*':
            match = number_1 * number_2
        elif sign == '/':
            match = number_1 // number_2
        
        
    return match

test_input = [
    'root: pppw + sjmn',
    'dbpl: 5',
    'cczh: sllz + lgvd',
    'zczc: 2',
    'ptdq: humn - dvpt',
    'dvpt: 3',
    'lfqf: 4',
    'humn: 5',
    'ljgn: 2',
    'sjmn: drzm * dbpl',
    'sllz: 4',
    'pppw: cczh / lfqf',
    'lgvd: ljgn * ptdq',
    'drzm: hmdt - zczc',
    'hmdt: 32',
]

monkeys = gat_dict(test_input)
number = get_number('sjmn',monkeys)
print(number)
print('pppw',monkeys)
eq_q = print_eq(monkeys,'pppw',[],[[]])
match = process_eq(eq_q,number)
print('sjmn',monkeys)


input_m = None
with open('input_21.txt','r') as file:
    input_m = file.readlines()


monkeys = gat_dict(input_m)

dat = monkeys.get('root')
p1 = dat.get('part1')
p2 = dat.get('part2')
number = get_number(p1,monkeys)
number_2 = get_number(p2,monkeys)
eq_q = print_eq(monkeys,p1,[],[[]])
match = process_eq(eq_q,number_2)
print('sjmn',monkeys)

print(number)
