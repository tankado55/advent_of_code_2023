import re

f = open("../inputs/input4.txt", "r")

cached_points = {}
cached_rec = {}
cards = []
for line in f:
    splitted = line.split(":")
    id = int(re.findall(r'\d+', splitted[0])[0])
    splitted = line.split("|")
    winnings =[int(x) for x in re.findall(r'\d+', splitted[0])]
    others = [int(x) for x in re.findall(r'\d+', splitted[1])]
    cards.append({"id": id, "winnings": winnings, "others": others})


def points(card):
    points = 0
    if card["id"] in cached_points:
        points = cached_points[card["id"]]
    else:
        for win in card["winnings"]:
            for oth in card["others"]:
                if win == oth:
                    points += 1
        cached_points[card["id"]] = points

    return points

def rec_points(card):
    sum = 0
    if str(card["id"]) in cached_rec:
        sum = cached_rec[card["id"]]
    else:
        pointss = points(card)
        queue = []
        sum = 1
        for i in range(pointss):
            queue.append(card["id"] + i)
        for q in queue:
            sum+= rec_points(q)

        cached_rec[str(card["id"])] = sum


    return pointss

sum2 = 0
cards_queue = cards.copy()
while len(cards_queue) > 0:
    card = cards_queue.pop(0)
    sum2 += rec_points(card)





print(sum2)

# 1118564485329252 high
# 483385564985111
# 12648035 ok
# 36349436
