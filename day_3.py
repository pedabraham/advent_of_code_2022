
input = None
with open('/Users/pedroam/advent_of_code_2022/input-3.txt','r') as file:
    input = file.readlines()

def get_priority(rucksack):
    # rucksack.strip()
    half = len(rucksack)/2
    i_1 = 0
    i_2 = int(half)
    priority = None
    comparment_1 = set()
    for l in range(int(half)):
        comparment_1.add(rucksack[i_1])
        i_1 += 1
    
    for l in range(int(half)):
        if rucksack[i_2] in comparment_1:
            priority = rucksack[i_2]
        i_2 += 1
    ord_priority = ord(priority)
    if ord_priority >= 97:
        return ord_priority - 96
    else:
        return ord_priority - 38

def compute(rucksack_list):
    total_points = 0
    for rucksack in rucksack_list:
        rucksack = rucksack.strip()
        points = get_priority(rucksack)
        total_points += points
    return total_points

example = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]


def get_priority2(rucksack1,rucksack2,rucksack3):
    priority = None
    comparment_1 = set()
    for element in rucksack1:
        comparment_1.add(element)
    comparment_2 = set()
    for element in rucksack2:
        comparment_2.add(element)
    for element in rucksack3:
        if element in comparment_2 and element in comparment_1:
            priority = element
        
    ord_priority = ord(priority)
    if ord_priority >= 97:
        return ord_priority - 96
    else:
        return ord_priority - 38

def compute_2(rucksack_list):
    total_points = 0
    for i in range(0,int(len(rucksack_list)),3):
        points = get_priority2(rucksack_list[i].strip(),rucksack_list[i+1].strip(),rucksack_list[i+2].strip())
        total_points += points
    return total_points

print(compute_2(example))