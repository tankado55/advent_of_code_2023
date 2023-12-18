f = open("../inputs/input2.txt", "r")

sum = 0
id = 0
eligible = False
for line in f:
    eligible = True
    id += 1
    game_data = line.split(":")[1]
    sets = game_data.split(";")
    color_max = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in sets:
        extractions = set.split(",")
        for extraction in extractions:
            number = extraction[1:].split(" ")[0]
            color = extraction[1:].split(" ")[1].replace("\n", "")
            if int(number) > color_max[color]:
                color_max[color] = int(number)
    power = color_max["red"] * color_max["green"] * color_max["blue"]
    sum += power

print(sum)
