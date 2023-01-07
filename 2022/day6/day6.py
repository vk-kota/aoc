from collections import Counter

with open('2022/day6/input.txt', 'r') as f:
    buffer = f.read()
    
for i in range(4, len(buffer)):
    sub_string = buffer[i-4:i]
    chars = Counter(sub_string)
    if len(chars.keys()) == 4:
        print(i)
        break

ans_1 = i

# Part Two
for i in range(14, len(buffer)):
    sub_string = buffer[i-14:i]
    chars = Counter(sub_string)
    if len(chars.keys()) == 14:
        print(i)
        break

ans_2 = i