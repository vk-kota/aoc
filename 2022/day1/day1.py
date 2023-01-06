

with open('day1/input.txt') as f:
    inp = f.readlines()

data = [line.replace('\n', '') for line in inp]

elves = {}
elves_counter = 1
cals = 0
for line in data:
    if line != '':
        cals += int(line)
    else:
        elves.update({str(elves_counter): cals})
        cals = 0
        elves_counter += 1

elves_sorted = {k: v
                for k, v in sorted(elves.items(),
                                   key=lambda item: item[1],
                                   reverse=True)}

ans_1 = next(iter(elves_sorted.values()))

ans_2 = sum(v for i, (k, v) in enumerate(elves_sorted.items()) if i < 3)