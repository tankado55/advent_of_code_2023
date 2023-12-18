import numpy as np

def is_valid(begin, end, l, m):
    to_check = m[l][begin:end+1]
    if (int(to_check) == 848):
        pass
    if l-1 > 0:
        up = m[l-1][np.clip(begin-1, 0, end+2):end+2]
        for c in up:
            if c != '.':
                return True
    if l+1 < len(m):
        down = m[l+1][np.clip(begin-1, 0, end+2):end+2]
        for c in down:
            if c != '.':
                return True
    if begin - 1 >= 0:
        if m[l][begin - 1] != '.':
            return True
    if end + 1 < len(m[l]):
        if m[l][end + 1] != '.':
            return True
    not_valid = m[l][begin:end+1]
    return False

f = open("../inputs/input3.txt", "r")

m = []
sum = 0
for i, l in enumerate(f):
    m.append(l.replace("\n", ""))

for i, l in enumerate(m):
    begin = None
    end = None
    for j, char in enumerate(l):
        if begin is None and char.isdigit():
            begin = j
        if begin is not None and char.isdigit():
            end = j
        if begin is not None and end is not None and char.isdigit() is False:
            if is_valid(begin, end, i, m):
                to_sum = int(m[i][begin:end+1])
                to_print = m[i].replace(m[i][begin:end + 1], '\033[92m' + m[i][begin:end + 1] + '\033[0m')
                print(to_print)
                sum += to_sum
            else:
                to_print = m[i].replace(m[i][begin:end+1], '\033[91m' + m[i][begin:end+1] + '\033[0m')
                print(to_print)
            begin = None
            end = None
        if begin is not None and end is not None and j >= len(l)-1:
            if is_valid(begin, end, i, m):
                to_sum = int(m[i][begin:end + 1])
                sum += to_sum




print(sum)

# low 536884
# 537732
# high 538217
