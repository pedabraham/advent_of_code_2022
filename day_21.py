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
    if number:
        return number
    else:
        monkey_1 = data.get('part1')
        monkey_2 = data.get('part2')
        number_1 = get_number(monkey_1,look_up)
        number_2 = get_number(monkey_2,look_up)
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
number = get_number('root',monkeys)
print(number)


input_m = None
with open('input_21.txt','r') as file:
    input_m = file.readlines()

monkeys = gat_dict(input_m)
number = get_number('root',monkeys)
print(number)
