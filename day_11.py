def get_rules(notes):
    monkeys = dict()
    current_monkey = None
    for note in notes:
        note = note.strip()
        note_parts = note.split()
        if not note_parts:
            continue
        if note_parts[0] == 'Monkey':
            monkeys[note_parts[1][0]] = {'items':[], 'operation':'', 'test_op':'', 'true':None, 'false':None , 'new_items':[], 'inspected':0}
            current_monkey = note_parts[1][0]
        if note_parts[0] == 'Starting':
            for i in range(2,len(note_parts)):
                if note_parts[i][-1] == ',':
                    number = int(note_parts[i][:-1])
                else:
                    number = int(note_parts[i])
                monkeys[current_monkey]['items'].append(number)
        if note_parts[0] == 'Operation:':
            sign = note_parts[-2]
            value = note_parts[-1]
            monkeys[current_monkey]['operation'] = {'sign':sign,'value':value}
        if note_parts[0] == 'Test:':
            monkeys[current_monkey]['test_op'] = int(note_parts[-1])
        if note_parts[0] == 'If':
            if note_parts[1] == 'true:':
                monkeys[current_monkey]['true'] = note_parts[-1]
            if note_parts[1] == 'false:':
                monkeys[current_monkey]['false'] = note_parts[-1]
    return monkeys

def process_monkeys(monkeys,relif):
    for monkey, rules in monkeys.items():
        items_back = rules['items']
        new_items = rules['new_items']

        operation_sign = rules['operation']['sign']
        operation_value = rules['operation']['value']
        test_op = rules['test_op']
        true_case = rules['true']
        false_case = rules['false']
        items_to_process = new_items + items_back
        for item_back in items_to_process:
            worry_level = get_worry_lavel(operation_sign,operation_value,item_back)
            if relif:
                worry_level = int(worry_level/3)
            if worry_level % test_op == 0:
                trow_monkey = monkeys[true_case]
                monkeys[true_case]['new_items'].append(worry_level)
            else:
                trow_monkey = monkeys[false_case]
                monkeys[false_case]['new_items'].append(worry_level)
        rules['inspected'] += len(items_to_process)
        if new_items:
            #rules['items'] = []
            rules['new_items'] = []

    for monkey, rules in monkeys.items():
        rules['items'] = rules['new_items']
        rules['new_items'] = []

def get_worry_lavel(operation_sign,operation_value,current_value):
    if operation_value == 'old':
        operation_value = current_value
    else:
        operation_value = int(operation_value)

    if operation_sign == '+':
        return operation_value + current_value
    elif operation_sign == '*':
        return operation_value * current_value
    else:
        return 0

def iterate(iterations,monkeys,relif):
    for i in range(iterations):
        process_monkeys(monkeys,relif)
    max_inspected = 0
    second_max_inspected = 0
    for monkey,params in monkeys.items():
        inspected = params['inspected']
        if inspected > max_inspected:
            if max_inspected > second_max_inspected:
                second_max_inspected = max_inspected
            max_inspected = inspected
        else:
            if inspected > second_max_inspected:
                second_max_inspected = inspected
    return max_inspected * second_max_inspected
                     

instructions_test = None
with open('test_11.txt','r') as file:
    instructions_test = file.readlines()

#monkeys = get_rules(instructions_test)
#value = iterate(20,monkeys,relif=True)
#print(value)

monkeys = get_rules(instructions_test)
value = iterate(10000,monkeys,relif=False)
print(value)


instructions = None
with open('input-9.txt','r') as file:
    instructions = file.readlines()

#monkeys = get_rules(instructions)
#value = iterate(20,monkeys,relif=True)
#print(value)

monkeys = get_rules(instructions)
value = iterate(10000,monkeys,relif=False)
print(value)