from typing import Set


count_sum = 0

with open('input.txt', 'r') as f:
    group: Set[str] = None
    for line in f:
        l = line.strip()
        if l:
            if group is None:
                group = set(l)
            else:
                group = group | set(l)
        else:
            count_sum += len(group)
            group = None
    count_sum += len(group)

print(f'Part 1: Sum = {count_sum}')

count_sum = 0

with open('input.txt', 'r') as f:
    group: Set[str] = None
    for line in f:
        l = line.strip()
        if l:
            if group is None:
                group = set(l)
            else:
                group = group & set(l)
        else:
            count_sum += len(group)
            group = None
    count_sum += len(group)

print(f'Part 2: Sum = {count_sum}')
