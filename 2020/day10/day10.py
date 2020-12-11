adapters = [0]

with open('sample2.txt', 'r') as f:
    adapters = adapters + sorted([int(line.strip()) for line in f])

adapters.append(adapters[-1] + 3)

one = 0
three = 0
for i in range (1, len(adapters)):
    diff = adapters[i] - adapters[i - 1]
    if diff == 1:
        one += 1
    elif diff == 3:
        three += 1
    else:
        raise ValueError()

print(f'ones {one} threes {three} answer: {one * three}')

# TODO: Part 2
opt = 0
for i in range(1, len(adapters) - 1):
    diff = adapters[i + 1] - adapters[i - 1]
    if diff <= 3:
        opt += 1

print(f'possible arrangements {2 ** opt}')
