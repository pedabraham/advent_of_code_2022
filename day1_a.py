calories_list = None
with open('input.txt','r') as file:
    calories_list = file.readlines()
print(calories_list[0].strip())
print(calories_list[0])

elf_with_max = None
elf_number = 1
local_calories_sum = 0
max_calories = 0
for calories in calories_list:
    if calories == '\n':
        if max_calories < local_calories_sum and local_calories_sum not in {69693,66757,64495}:
            max_calories = local_calories_sum
            elf_with_max = elf_number
        local_calories_sum = 0
        elf_number += 1
    else:
        local_calories_sum += int(calories)
if max_calories < local_calories_sum:
    max_calories = local_calories_sum
    elf_with_max = elf_number
print(elf_with_max)
print(elf_number)
print(len(calories_list))
print(max_calories)