import numpy
import random

KEY_LEN = 38

def is_found_full(arr):
    # print(arr)
    for i in arr:
        if i == 0:
            return False
    return True

init = numpy.zeros((KEY_LEN,11), dtype=int)
found = numpy.zeros(KEY_LEN, dtype=int)

for i in range(init.shape[0]):
    init[i][0] = i+1

print(init)

i = 0
coins = 8
while is_found_full(found) == False:
    random.seed(i + coins)
    for row in init:
        random.shuffle(row)

    # print(init)

    result = ""
    for row in init:
        # print(row)
        a = random.choice(row)
        # print(a)
        if a > 0:
            found[a-1] = 1
        result += str(a) + " "
    print(i, result)
    i += 1

# print(init)