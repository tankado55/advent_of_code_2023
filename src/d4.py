import re

f = open("../inputs/input4.txt", "r")

table = []

for line in f:
    table.append(line.split(":")[1])
winnings = []
others = []
for line in table:
    splitted = line.split("|")
    test = splitted[0].split(" ")
    winnings.append([int(x) for x in re.findall(r'\d+', splitted[0])])
    others.append([int(x) for x in re.findall(r'\d+', splitted[1])])

sum = 0
for i in range(len(table)):
    points = 0
    for j in range(len(winnings[i])):
        for k in range(len(others[i])):
            if winnings[i][j] == others[i][k]:
              if points == 0: points +=1
              else: points *=2

    sum+=points

print(sum)

