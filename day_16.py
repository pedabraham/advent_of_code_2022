from pprint import pformat
from copy import deepcopy

def generate_map(instructions):
    valves = dict()
    with_value = set()
    for instruction in instructions:
        instruction = instruction.strip()
        data = instruction.split()
        valve = data[1]
        tunnels = data[9:]
        rate = data[4]
        rate = int(rate[5:-1])
        if rate>0:
            with_value.add(valve)
        valves[valve] = {'tunnels':tunnels,'rate':rate}
    return valves, with_value

def get_distancel(start,end):

    pass

class Node():
    def __init__(self,value,distance):
        self.value = value
        self.distance = distance
        self.next = None


def get_distance(valve_map,start,good_tunnels):
    node_start = Node(start,0)
    distance = 0
    back = node_start
    visited = set()
    visited.add(start)
   
    front = node_start
    print_distance = 0
    found = dict()
    while (front):
        valve = front.value
        data = valve_map.get(valve)

        distance = front.distance
        if valve in good_tunnels and valve not in found:
            #valve_rate = valve_map.get(valve).get('rate')
            #found[valve] = (time-distance-1) * valve_rate
            found[valve] = distance
        
        if len(found) == len(good_tunnels):
            break

        tunnels = data.get('tunnels')
        for tunnel in tunnels:
            tunnel = tunnel.strip(',')
            if tunnel not in visited:
                back.next = Node(tunnel,front.distance + 1)
                back = back.next
                visited.add(tunnel)
        front = front.next
    return found
        



input_t = [
    'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
    'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
    'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
    'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
    'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
    'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
    'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
    'Valve HH has flow rate=22; tunnel leads to valve GG',
    'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
    'Valve JJ has flow rate=21; tunnel leads to valve II  ',
]


def record_possible_ditances(start,valve_map,good_paths):
    distance_record = dict()
    distances = get_distance(valve_map,start,good_paths)
    distance_record[start] = distances
    for valve in good_paths:
        distances = get_distance(valve_map,valve,good_paths)
        distance_record[valve] = distances
    return distance_record

def get_sum(start,end):
    minute_sum = 0
    for i in range(start,end+1):
        minute_sum += 1
    return minute_sum

def calcultate_all_paths(distance_record,start,valve_map):
    pass
    possible_nodes = distance_record.get(start) 
    len_nodes = len(possible_nodes)
    if len_nodes > 30:
        len_nodes = 30
    permutations = [{'last_node':start}]
    for i in range(30):
        new_permutations = []
        min_30 = True
        min_time = None
        for permutation in permutations:
           
            for node in possible_nodes:
                path = permutation.get('path') or set()
                pressure = permutation.get('pressure') or 0
                rate = valve_map.get(node).get('rate')
                time = permutation.get('time') or 30
                last_node = permutation.get('last_node')
                sum_pressure = permutation.get('sum_pressure') or 0
                if node not in path and time:
                    new_path = deepcopy(path)
                    new_path.add(node)
                    distances = distance_record.get(last_node)
                    distance = distances.get(node)
                    remainnig_time = time - distance -1


                    if remainnig_time < 0:
                        continue
                    else:
                        min_30 = False
                        sum_pressure += (time-remainnig_time) * (pressure)

                    if len_nodes == len(new_path):
                        sum_pressure += (remainnig_time) * (pressure + rate)
                        remainnig_time = 0

                    new_permutations.append({'path':new_path, 'pressure':pressure+rate, 'time':remainnig_time, 'last_node':node, 'sum_pressure':sum_pressure})
        if min_30:
            print('3090')
            break
        print(f'{i}: {len(new_permutations)}')
        permutations = new_permutations
    #print(permutations)
    
    max_pressure = 0
    for permutation in permutations:
        total_pressure = permutation.get('sum_pressure')
        if max_pressure < total_pressure:
            max_pressure = total_pressure

   
    print(max_pressure)


start = 'AA'
valves,vals = generate_map(input_t)
#print(pformat(valves))
#distances = get_distance(valves,'JJ',vals)
#print(pformat(distances))
distance_record = record_possible_ditances('AA',valves,vals)
print(pformat(distance_record))
calcultate_all_paths(distance_record,'AA',valves)


input_m = None
with open('input-11.txt','r') as file:
    input_m = file.readlines()

start = 'AA'
valves,vals = generate_map(input_m)
#print(pformat(valves))
#distances = get_distance(valves,'JJ',vals)
#print(pformat(distances))
distance_record = record_possible_ditances(start,valves,vals)
#print(pformat(distance_record))
calcultate_all_paths(distance_record,start,valves)


def get_pressures(valve_map,good_paths,start,time,distance_record,pressure,c_pressure):







    distances = distance_record.get(start)
    if not distances:
        distances = get_distance(valves,start,good_paths)
        distance_record[start] = distances
    if len(distances) == 1:
        for valve,distance in distances.items():
            valve_rate = valve_map.get(valve).get('rate')
            pressure[valve] += get_sum(time-distance,time) * c_pressure
            c_pressure = c_pressure + valve_rate
            pressure[valve] += (time-distance-1) * valve_rate
            pressure[valve] += get_sum(0,time-distance-2) * valve_rate



    
    pressure = dict()
    time = 30
    for valve,distance in distances.items():
        valve_rate = valve_map.get(valve).get('rate')
        pressure[valve] = (time-distance-1) * valve_rate
        paths = deepcopy(good_paths)
        paths.pop(valve)
        new_pressures = get_pressures(valve_map,paths,valve,time-distance-1,distance_record)
        max_pressure = 0
        max_valve = None
        for n_valve,new_pressure in new_pressures.items:
            if new_pressure > max_pressure:
                max_pressure = new_pressure
                max_valve = n_valve
        pressure[valve] += max_pressure 
        

