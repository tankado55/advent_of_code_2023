import numpy as np

def is_valid(begin, end, l, m, gear_dict, to_sum):
    to_check = m[l][begin:end+1]
    if l-1 > 0:
        up = m[l-1][begin-1:end+2]
        for i, c in enumerate(up):
            if c == '*':
                key = str(l-1) + "x" + str(begin + i - 1)
                if key in gear_dict:
                    gear_dict[key][0] += 1
                    gear_dict[key][1] *= to_sum
                else:
                    gear_dict[key] = []
                    gear_dict[key].append(1)
                    gear_dict[key].append(to_sum)
                return
    if l+1 < len(m):
        down = m[l+1][begin-1:end+2]
        for i, c in enumerate(down):
            if c == '*':
                key = str(l+1) + "x" + str(begin + i - 1)
                if key in gear_dict:
                    gear_dict[key][0] += 1
                    gear_dict[key][1] *= to_sum
                else:
                    gear_dict[key] = []
                    gear_dict[key].append(1)
                    gear_dict[key].append(to_sum)
                return

    if m[l][begin - 1] == '*':
        key = str(l) + "x" + str(begin - 1)
        if key in gear_dict:
            gear_dict[key][0] += 1
            gear_dict[key][1] *= to_sum
        else:
            gear_dict[key] = []
            gear_dict[key].append(1)
            gear_dict[key].append(to_sum)
        return

    if m[l][end + 1] == '*':
        key = str(l) + "x" + str(end+1)
        if key in gear_dict:
            gear_dict[key][0] += 1
            gear_dict[key][1] *= to_sum
        else:
            gear_dict[key] = []
            gear_dict[key].append(1)
            gear_dict[key].append(to_sum)
        return

    return

f = open("../inputs/input3.txt", "r")

gear_dict = {}
m = []
sum = 0
for l in f:
    m.append('.' + l.replace("\n", "") + '.')

for i, l in enumerate(m):
    begin = None
    end = None
    for j, char in enumerate(l):
        if begin is None and char.isdigit():
            begin = j
        if begin is not None and char.isdigit():
            end = j
        if begin is not None and end is not None and char.isdigit() is False:
            to_sum = int(m[i][begin:end + 1])
            is_valid(begin, end, i, m, gear_dict, to_sum)
            begin = None
            end = None

for summing in gear_dict.keys():
    if gear_dict[summing][0] > 1:
        sum += gear_dict[summing][1]

print(sum)
