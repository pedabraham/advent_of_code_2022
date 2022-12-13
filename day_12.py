import os
import time

def get_level_map(input_map):
    level_map = list()
    row = 0
    start = None
    end = None
    for line in input_map:
        line = line.strip()
        col = 0
        line_levels = list()
        for letter in line:
            level = ord(letter) - 96
            if letter == 'S':
                start = (row,col)
                level = 1
            if letter == 'E':
                end = (row,col)
                level = 26
            line_levels.append(level)
            col += 1
        level_map.append(line_levels)
        row += 1
    return {'start':start,'end':end,'map':level_map}

class Node():
    def __init__(self,value,distance):
        self.value = value
        self.distance = distance
        self.next = None

def get_distance(level_map,start,end):
    if (start[0],start[1]) == end:
        return 0
    node_start = Node(start,0)
    distance = 0
    back = node_start
    visited = set()
    visited.add(start)
    rows = len(level_map)
    cols = len(level_map[0])
    front = node_start
    print_distance = 0
    while (front):
        position = front.value
        distance = front.distance
        if level_map[position[0]][position[1]] == 26:
                return front.distance 
        current_level = level_map[position[0]][position[1]]
        posible_paths = list()

        # up
        if position[0] > 0 and level_map[position[0] - 1][position[1]] - current_level <= 1:
            posible_paths.append((position[0] - 1,position[1]))
        # down
        if position[0] < rows - 1 and level_map[position[0] + 1][position[1]] - current_level <= 1:
            posible_paths.append((position[0] + 1,position[1]))
        #left
        if position[1] > 0 and level_map[position[0]][position[1] - 1] - current_level <= 1:
            posible_paths.append((position[0],position[1] - 1))
        # right 
        if position[1] < cols - 1 and level_map[position[0]][position[1] + 1] - current_level <= 1:
            posible_paths.append((position[0],position[1] + 1))
        for cordenate in posible_paths:
            if cordenate not in visited:
                back.next = Node(cordenate,front.distance + 1)
                back = back.next
                visited.add(cordenate)
        front = front.next
        #if distance != print_distance:
        #    for row in range(rows):
        #        for col in range(cols):
        #            if (row,col) in visited:
        #                print('.', end='')
        #            else:
        #                print(chr(level_map[row][col]+96), end='')
        #        print()
        #    print_distance = distance
        #    print(distance)
        #    #time.sleep(.1)
        #    if distance > 475:
        #        time.sleep(3)
        #    os.system('clear')
    print(distance)
    print(chr(current_level+96))

input_test = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi',
]

data = get_level_map(input_test)
#print(data)
distance = get_distance(data['map'],data['start'],data['end'])
print(distance)

input_map = None
with open('input-10.txt','r') as file:
    input_map = file.readlines()
data = get_level_map(input_map)
#print(data)

rows = len(data['map'])
min_dis = None
for row in range(rows):
    distance = get_distance(data['map'],(row,0),data['end'])
    if not min_dis or min_dis > distance:
        min_dis = distance
print(min_dis)