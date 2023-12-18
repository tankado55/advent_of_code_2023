f = open("../inputs/input1.txt", "r")

spelled_to_digit = {
    "seven": "seven7seven",
    "nine": "nine9nine",
    "one": "one1one",
    "eight": "eight8eight",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
}


cal_sum = 0
for l in f:
    first = None
    last = None
    for key in spelled_to_digit:
        l = l.replace(key, spelled_to_digit[key])
    for c in l:
        if c.isnumeric():
            if first is None:
                first = c
            last = c
    cal = str(first) + str(last)
    cal_sum += int(cal)
print(cal_sum)
