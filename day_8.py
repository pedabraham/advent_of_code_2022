def get_map(input):
    tree_map = list()
    for line in input:
        line_list = []
        line = line.strip()
        for number in line:
            line_list.append(int(number))
        tree_map.append(line_list)
    return tree_map

def is_visible(row_t,col_t,tree_map):
    rigth_limit = int(len(tree_map[0]))
    down_limit = int(len(tree_map))
    # row 1 col 1
    down = True
    up = True
    left = True
    right = True
    for row in range(row_t+1,down_limit):
        if tree_map[row_t][col_t] <= tree_map[row][col_t]:
            down = False
            break
    for row in range(0,row_t):
        if tree_map[row_t][col_t] <= tree_map[row][col_t]:
            up = False
            break
    for col in range(col_t+1,rigth_limit):
        if tree_map[row_t][col_t] <= tree_map[row_t][col]:
            right = False
            break
    for col in range(0,col_t):
        if tree_map[row_t][col_t] <= tree_map[row_t][col]:
            left = False
            break
    if down or up or left or right:
        return True
    return False

def get_score(row_t,col_t,tree_map):
    rigth_limit = int(len(tree_map[0]))
    down_limit = int(len(tree_map))
    # row 1 col 1
    down = down_limit-row_t-1
    up = row_t
    left = col_t 
    right = rigth_limit-col_t-1
    for row in range(row_t+1,down_limit):
        if tree_map[row_t][col_t] <= tree_map[row][col_t]:
            down = row-row_t
            break
    for row in range(row_t-1,0,-1):
        if tree_map[row_t][col_t] <= tree_map[row][col_t]:
            up = row_t-row
            break
    for col in range(col_t+1,rigth_limit):
        if tree_map[row_t][col_t] <= tree_map[row_t][col]:
            right = col - col_t
            break
    for col in range(col_t-1,0,-1):
        if tree_map[row_t][col_t] <= tree_map[row_t][col]:
            left = col_t - col
            break
    return down * up * left * right


def process_map(tree_map):
    cols = int(len(tree_map[0]))
    rows = int(len(tree_map))
    valids = 0
    for row in range(rows):
        if row in {0,rows-1}:
            valids += rows
            continue
        for col in range(cols):
            if col in {0,cols-1}:
                valids += 1
                continue
            visible = is_visible(row,col,tree_map)
            if visible:
                valids += 1
    return valids

def process_views(tree_map):
    cols = int(len(tree_map[0]))
    rows = int(len(tree_map))
    valids = 0
    max_score = 0
    for row in range(rows):
        if row in {0,rows-1}:
            continue
        for col in range(cols):
            if col in {0,cols-1}:
                continue
            score = get_score(row,col,tree_map)
            if score > max_score :
                max_score = score
    return max_score


test = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

map_test = get_map(test)
#valids = process_map(map_test)
max_score = process_views(map_test)
print(max_score)
#print(valids)

input_t = None
with open('input-6.txt','r') as file:
    input_t = file.readlines()

map_t = get_map(input_t)
max_score = process_views(map_t)
print(max_score)
#valids = process_map(map_t)
#print(valids)