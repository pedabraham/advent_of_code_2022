#part 1
def is_contained(pair1,pair2):
    min = None
    if int(pair1[0]) == int(pair2[0]):
        return True

    if int(pair1[0]) >= int(pair2[0]):
        min_s = pair2[0]
        min_f = int(pair2[1])
        max_s = pair1[0]
        max_f = int(pair1[1])
    else:
        min_s = int(pair1[0])
        min_f = int(pair1[1])
        max_s = int(pair2[0])
        max_f = int(pair2[1])

    if max_f <= min_f:
        return True
    return False

#part 2
def overlap(pair1,pair2):
    min = None
    if int(pair1[0]) == int(pair2[0]):
        return True

    if int(pair1[0]) >= int(pair2[0]):
        min_s = int(pair2[0])
        min_f = int(pair2[1])
        max_s = int(pair1[0])
        max_f = int(pair1[1])
    else:
        min_s = int(pair1[0])
        min_f = int(pair1[1])
        max_s = int(pair2[0])
        max_f = int(pair2[1])

    if max_f <= min_f or max_s <= min_f:
        return True
    return False


elves_pairs = None
with open('input-4.txt','r') as file:
    elves_pairs = file.readlines()

count = 0
a = 0
for elves in elves_pairs:
    elves = elves.strip()
    pairs = elves.split(',')
    pair1 = pairs[0].split('-')
    pair2 = pairs[1].split('-')
    if overlap(pair1,pair2):
        count += 1
    a += 1


print(len(elves_pairs))
