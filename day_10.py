def sum_signals(instructions):
    cycles = 1
    screen_sum = 1
    strenght_sum = 0
    cycle_passed = {40,80,120,160,200,240} 
    sums = list()
    number = 1
    i = 0
    for instruction in instructions:
        i += 1
        instruction = instruction.strip()
        data = instruction.split()
        command = data[0]
        if cycles in {99,100,101,102}:
            print(0)
        if command == 'noop':
            cycles += 1
        else:
            number= int(data[1])
            screen_sum += number
            cycles += 2
        if cycles % 20 == 0 and cycles not in cycle_passed:
            strenght_sum += cycles * screen_sum
            cycle_passed.add(cycles)
            sums.append(cycles * screen_sum)
        if cycles % 20 == 1  and cycles-1 not in cycle_passed:
            strenght_sum += (cycles-1) * (screen_sum-number)
            cycle_passed.add(cycles-1)
            sums.append((cycles-1) * (screen_sum-number))
        
    print(sums)
    return strenght_sum

def draw_crt(instructions):
    cycles = 0
    screen_sum = 1
    strenght_sum = 0
    cycle_passed = {40,80,120,160,200,240} 
    sums = list()
    number = 1
    i = 0
    #print('#', end='')
    pixels = 0
    for instruction in instructions:
        i += 1
        
        instruction = instruction.strip()
        data = instruction.split()
        command = data[0]
        if command == 'noop':
            print_screen(pixels,screen_sum,cycles)
            
            cycles += 1
            pixels = get_pixels(pixels,cycles)

        else:
            print_screen(pixels,screen_sum,cycles)

            cycles +=1
            pixels = get_pixels(pixels,cycles)

            print_screen(pixels,screen_sum,cycles)
            number= int(data[1])
            screen_sum += number
            cycles += 1
            pixels = get_pixels(pixels,cycles)

            
#            print_screen(pixels,screen_sum,cycles)

      

def get_pixels(pixels,cycles):
    if cycles % 40 == 0:
        return 0
    else:
        return pixels + 1

def print_screen(pixels,screen_sum,cycles):
    if pixels == 0:
        print()
    if pixels >= screen_sum -1 and pixels < screen_sum + 2:
        print('#', end='')    
    else:
        print('.',end='')

instructions = None
with open('input-8.txt','r') as file:
    instructions = file.readlines()

instructions_test = None
with open('test_10.txt','r') as file:
    instructions_test = file.readlines()

strenght = sum_signals(instructions_test)
print(strenght)


draw_crt(instructions_test)
print()
print()
draw_crt(instructions)

