assignments = []
with open('2022/day4/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        assigns = line.split(',')
        start_ends = [assign.split('-') for assign in assigns]
        start_ends = start_ends[0] + start_ends[1]
        start_ends = [int(number) for number in start_ends]
        assignments.append(start_ends)


def check_subset(assignment: list) -> bool:
    if assignment[0] >= assignment[2] and assignment[1] <= assignment[3]:
        return True
    elif assignment[2] >= assignment[0] and assignment[3] <= assignment[1]:
        return True
    else:
        return False


overlaps = [1 for assignment in assignments if check_subset(assignment)]
n_overlaps = sum(overlaps)

# Part 2
def check_overlap(assignment: list) -> bool:
    elf_1 = set(range(assignment[0], assignment[1] + 1))
    elf_2 = set(range(assignment[2], assignment[3] + 1))
    return len(elf_1.intersection(elf_2)) != 0

overlaps = [1 for assignment in assignments if check_overlap(assignment)]
n_overlaps = sum(overlaps)