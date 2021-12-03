with open('input') as f:
    lines = [l.strip() for l in f.readlines()]

line_size = len(lines[0])

zeros = [0] * line_size
ones = [0] * line_size

for line in lines:
    for i in range(line_size):
        match line[i]:
            case '0':
                zeros[i] += 1
            case '1':
                ones[i] += 1

gamma = ''
epsilon = ''

for i in range(line_size):
    if zeros[i] > ones[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

part1 = int(gamma, 2) * int(epsilon, 2)

idx = 0
rest = lines
while len(rest) > 1:
    zeros = ones = 0
    for line in rest:
        match line[idx]:
            case '0':
                zeros += 1
            case '1':
                ones += 1
    if zeros > ones:
        rest = [r for r in rest if r[idx] == '0']
    else:
        # more ones, so keep ones
        rest = [r for r in rest if r[idx] == '1']
    idx += 1

generator = rest.pop()

idx = 0
rest = lines
while len(rest) > 1:
    zeros = ones = 0
    for line in rest:
        match line[idx]:
            case '0':
                zeros += 1
            case '1':
                ones += 1
    if ones < zeros:
        rest = [r for r in rest if r[idx] == '1']
    else:
        # less zeros, so keep zeros
        rest = [r for r in rest if r[idx] == '0']
    idx += 1

scrubber = rest.pop()

part2 = int(generator, 2) *int(scrubber, 2)
