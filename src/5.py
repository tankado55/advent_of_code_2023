import re
import sys

def map_to(l, r, maps):
    current_mapped_seed = [(l, r)]

    # phase 1
    for map in maps:
        previous_mapped_seed = current_mapped_seed
        current_mapped_seed = []
        while len(previous_mapped_seed) > 0:
            seed = previous_mapped_seed.pop()
            found = 0
            for map_line in map.split("\n")[1:]:
                map_line_comp = [int(x) for x in re.findall(r'\d+', map_line)]
                diff = map_line_comp[0] - map_line_comp[1]
                map_l = map_line_comp[1]
                map_r = map_line_comp[1] + map_line_comp[2] - 1

                if seed[0] >= map_line_comp[1] and seed[1] <= map_r:
                    current_mapped_seed.append((seed[0] + diff, seed[1] + diff))
                    found = 1
                    print("mapped " + str(seed[0]) + ", " + str(seed[1]) + " TO " + str(seed[0] + diff) + ", " + str(
                        seed[1] + diff))
                    break
                elif seed[1] < map_l:
                    pass
                elif seed[0] > map_r:
                    pass
                elif seed[0] >= map_line_comp[1] and seed[1] > map_r: # r is out
                    current_mapped_seed.append((seed[0] + diff, map_r + diff))
                    previous_mapped_seed.append((map_r+1, seed[1]))
                    found = 1
                    print("mapped " + str(seed[0]) + ", " + str(map_r) + " TO " + str(seed[0] + diff) + ", " + str(
                        map_r + diff))
                    break
                elif seed[0] < map_line_comp[1] and seed[1] <= map_r: # l is out
                    current_mapped_seed.append((map_l + diff, seed[1] + diff))
                    previous_mapped_seed.append((seed[0], map_l-1))
                    found = 1
                    print("mapped " + str(map_l) + ", " + str(seed[1]) + " TO " + str(map_l + diff) + ", " + str(seed[1] + diff))
                    break
            if found == 0:
                current_mapped_seed.append((seed[0], seed[1]))
                print("mapped SAME: " + str(seed[0]) + str(seed[1]))

    return current_mapped_seed



def main():
    f = open("../inputs/input5.txt", "r")
    seeds = [int(x) for x in re.findall(r'\d+', f.readline().split(":")[1])]
    maps = f.read().strip().split("\n\n")

    even_indexes = range(0, len(seeds), 2)
    mapped = []
    for seed_idx in even_indexes:
        seed = seeds[seed_idx]
        l = seed
        r = seed + seeds[seed_idx + 1]
        mapped.append(map_to(l, r, maps))


    to_print = [element[0] for row in mapped for element in row]

    print(min(to_print))


if __name__ == "__main__":
    main()


# 79874952 too high
# 79874951
