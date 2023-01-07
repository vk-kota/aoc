import re
import struct
from itertools import groupby
from collections import Counter
import numpy as np

lines = []
with open('2022/day5/input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))

stacks = []
instructions = []
groups = []

for _, g in groupby(lines, lambda line: line == ''):
    groups.append(list(g))

stacks, _, instructions = groups
stacks_p = []
for line in stacks[:-1]:
    linewidth = len(line)
    line = [line[n:n+3] for n in range(0, linewidth, 4)]
    line = [re.sub(r'\s{2,}', '', item) for item in line]
    stacks_p.append(line)

stacks_arr = np.array(stacks_p)

def process_instruction(inx: str, stacks_arr: np.array):
    new_stacks_arr = stacks_arr.copy()
    move, start, end = [int(num) for num in re.findall(r'(?<=\s)\d+', inx)]
    n_crates, n_stacks = new_stacks_arr.shape
    to_stack = new_stacks_arr[:, end-1]
    end_stack_space = Counter(to_stack)['']
    if move > end_stack_space:
        new_rows = np.full((move - end_stack_space, n_stacks), '')
        new_stacks_arr = np.append(new_rows, stacks_arr, axis=0)

    from_stack = stacks_arr[:, start-1]
    try:
        from_stack_start = np.argwhere(from_stack == '')[-1][0] + 1
    except IndexError:
        from_stack_start = 0

    move_stack = from_stack[from_stack_start:from_stack_start + move][::-1]
    new_stacks_arr[from_stack_start + max(0, move - end_stack_space)
                   :from_stack_start + max(0, move - end_stack_space) + move,
    start-1] = ''
    to_stack_start = np.argwhere(new_stacks_arr[:, end-1] == '')[-1][0] + 1 - move
    new_stacks_arr[to_stack_start: to_stack_start + move, end-1] = move_stack

    return new_stacks_arr

prev = stacks_arr
for inx in instructions:
    new = process_instruction(inx, prev)
    prev = new

tops = []
for c in range(0, new.shape[-1]):
    tops.append(new[np.argwhere(new[:, c] == '')[-1] + 1, c][0])

tops = [re.findall(r'\w+', top)[0] for top in tops]
ans_1 = ''.join(tops)

# Part Two
def process_instruction(inx: str, stacks_arr: np.array):
    new_stacks_arr = stacks_arr.copy()
    move, start, end = [int(num) for num in re.findall(r'(?<=\s)\d+', inx)]
    n_crates, n_stacks = new_stacks_arr.shape
    to_stack = new_stacks_arr[:, end-1]
    end_stack_space = Counter(to_stack)['']
    if move > end_stack_space:
        new_rows = np.full((move - end_stack_space, n_stacks), '')
        new_stacks_arr = np.append(new_rows, stacks_arr, axis=0)

    from_stack = stacks_arr[:, start-1]
    try:
        from_stack_start = np.argwhere(from_stack == '')[-1][0] + 1
    except IndexError:
        from_stack_start = 0

    move_stack = from_stack[from_stack_start:from_stack_start + move]
    new_stacks_arr[from_stack_start + max(0, move - end_stack_space)
                   :from_stack_start + max(0, move - end_stack_space) + move,
    start-1] = ''
    to_stack_start = np.argwhere(new_stacks_arr[:, end-1] == '')[-1][0] + 1 - move
    new_stacks_arr[to_stack_start: to_stack_start + move, end-1] = move_stack

    return new_stacks_arr

prev = stacks_arr
for inx in instructions:
    new = process_instruction(inx, prev)
    prev = new

tops = []
for c in range(0, new.shape[-1]):
    tops.append(new[np.argwhere(new[:, c] == '')[-1] + 1, c][0])

tops = [re.findall(r'\w+', top)[0] for top in tops]
ans_2 = ''.join(tops)
