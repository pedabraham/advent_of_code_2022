def generate_tree(commands):
    filesystem = {'files': 0,'parent':None}
    main_parent = filesystem
    parent = main_parent
    for command in commands:
        command = command.strip()
        if command == '$ cd /':
            parent = main_parent
        elif command == '$ ls':
            continue
        elif command == '$ cd ..':
            parent = parent['parent']
        elif '$ cd' in command:
            parent_dir_name = command.split('$ cd')[1]
            parent = parent[parent_dir_name]
        elif 'dir' in command:
            dir_name = command.split('dir')[1]
            parent[dir_name] = {'files': 0,'parent':parent}
        else:
            space = command.split()[0]
            space = int(space)
            parent['files'] += space
    return filesystem

def get_local_sum(filesystem,global_sum):
    sum = filesystem['files']
    for element,data in filesystem.items():
        if element in {'files','parent'}:
            continue
        local_sum = get_local_sum(data,global_sum)
        sum += local_sum
        if local_sum < 100000:
            global_sum.append(local_sum)
    return sum

def get_local_sum_smallest(filesystem,smallest, threshold):
    sum = filesystem['files']
    for element,data in filesystem.items():
        if element in {'files','parent'}:
            continue
        local_sum = get_local_sum_smallest(data,smallest,threshold)
        sum += local_sum
        if local_sum > threshold:
            if not smallest[0] or local_sum < smallest[0]:
                smallest[0] = local_sum
    return sum

coms = [
'$ cd /',
'$ ls',
'dir a',
'14848514 b.txt',
'8504156 c.dat',
'dir d',
'$ cd a',
'$ ls',
'dir e',
'29116 f',
'2557 g',
'62596 h.lst',
'$ cd e',
'$ ls',
'584 i',
'$ cd ..',
'$ cd ..',
'$ cd d',
'$ ls',
'4060174 j',
'8033020 d.log',
'5626152 d.ext',
'7214296 k',]

fs = generate_tree(coms)

gs = []
get_local_sum(fs,gs)

sum = 0
for local_sum in gs:
    sum += local_sum


#from pformat import pprint
print(fs)
print(gs)
print(sum)

# real input
commands_in = None
with open('input-5.txt','r') as file:
    commands_in = file.readlines()

fs = generate_tree(commands_in)

gs = []
space = get_local_sum(fs,gs)

sum = 0
for local_sum in gs:
    sum += local_sum

unused = 70000000 - space
needed = 30000000 - unused
smallest = [None]
get_local_sum_smallest(fs,smallest, needed)

#from pformat import pprint
print(fs)
print(gs)
print(space)
print(sum)
print(smallest)