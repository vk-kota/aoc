from typing import Union
from string import ascii_letters
from array import array

PRIORITY_MAP = {k: v for k, v in zip(ascii_letters, range(1, 53))}

rucks = []
with open('2022/day3/input.txt', 'r') as f:
    for sack in f.readlines():
        ruck = sack.strip('\n')
        assert len(ruck) % 2 == 0
        cpts = (ruck[:int(len(ruck) / 2)], ruck[int(len(ruck) / 2):])
        rucks.append(cpts)


def find_common(ruck: Union[tuple, str]) -> str:
    c_1, c_2 = ruck
    try:
        return list(set(c_1).intersection(set(c_2)))[0]
    except IndexError:
        print((c_1, c_2))


priorities = [int(PRIORITY_MAP[find_common(ruck)]) for ruck in rucks]
priorities_arr = array('i')
priorities_arr.fromlist(priorities)
total = sum(priorities_arr)

# Part 2
rucks = []
with open('2022/day3/input.txt', 'r') as f:
    for sack in f.readlines():
        ruck = sack.strip('\n')
        rucks.append(ruck)

def find_badge(sacks: Union[list, str]) -> str:
    sacks_set = [set(sack) for sack in sacks]
    common = sacks_set[0].intersection(sacks_set[1]).intersection(sacks_set[2])
    return list(common)[0]

badges = [find_badge(rucks[n:n+3]) for n in range(0, len(rucks), 3)]
priorities = [int(PRIORITY_MAP[badge]) for badge in badges]
priorities_arr = array('i')
priorities_arr.fromlist(priorities)
total = sum(priorities_arr)
