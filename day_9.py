from math import sqrt

def calculate_tail_moves(simulation):
    t_trace = set()
    t_trace.add((0,0))
    h_position = [0,0]
    t_position = [0,0]
    for step in simulation:
        step = step.strip()
        vector = step.split()
        direction = vector[0]
        magnitud = int(vector[1])
        if direction == 'R':
            h_position[0] += magnitud
        if direction == 'L':
            h_position[0] -= magnitud
        if direction == 'U':
            h_position[1] += magnitud
        if direction == 'D':
            h_position[1] -= magnitud

            
        x_diff = int(sqrt((h_position[0] - t_position[0]) ** 2))
        y_diff = int(sqrt((h_position[1] - t_position[1]) ** 2))
        if x_diff <= 1 and y_diff <= 1:
            # t didnt move
            continue
        # t move

        if direction == 'R':
            for i in range(1,x_diff):
                t_trace.add((t_position[0]+i,h_position[1]))
            t_position = [t_position[0]+i,h_position[1]]
        if direction == 'L':
            for i in range(1,x_diff):
                t_trace.add((t_position[0]-i,h_position[1]))
            t_position = [t_position[0]-i,h_position[1]]
        if direction == 'U':
            for i in range(1,y_diff):
                t_trace.add((h_position[0],t_position[1]+i))
            t_position = [h_position[0],t_position[1]+i]
        if direction == 'D':
            for i in range(1,y_diff):
                t_trace.add((h_position[0],t_position[1]-i))
            t_position = [h_position[0],t_position[1]-i]
        op = 2*2
    return len(t_trace)

test = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2',
]

test_2 = [
    'U 1',
    'D 1',
    'L 1',
    'U 2',
]



moves = calculate_tail_moves(test_2)
print(moves)

simulation = None
with open('input-7.txt','r') as file:
    simulation = file.readlines()

moves = calculate_tail_moves(simulation)
print(moves)