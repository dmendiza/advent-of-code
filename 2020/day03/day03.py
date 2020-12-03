from typing import List


def get_data() -> List[str]:
    data = list()
    with open('input.txt', 'r') as f:
        for line in f:
            data.append(line.strip('\n'))
    return data

x = 0
tree_count = 0
for row in get_data():
    if row[x] == '#':
        tree_count += 1
    x = (x + 3) % len(row)

print(f'Part 1: Encountered {tree_count} trees')

# Part 2
def count_trees_in_slope(right: int, down: int) -> int:
    x = 0
    tree_count = 0
    data = get_data()[::down]
    for row in data:
        if row[x] == '#':
            tree_count += 1
        x = (x + right) % len(row)
    return tree_count

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

product = 1

for slope in slopes:
    product *= count_trees_in_slope(*slope)

print(f'Part 2: Product of all slopes {product}')
