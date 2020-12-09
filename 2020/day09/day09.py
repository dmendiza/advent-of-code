from typing import List, Tuple


preamble: List[int] = list()
preamble_len = 25


def addends_in_preamble(num: int, preamble: List[int]) -> bool:
    for i, x in enumerate(preamble):
        diff = num - x
        for y in preamble[i + 1:]:
            if y == diff:
                return True
    return False


with open('input.txt', 'r') as f:
    for _ in range(preamble_len):
        preamble.append(int(f.readline().strip()))
    for line in f:
        num = int(line.strip())
        if addends_in_preamble(num, preamble):
            _ = preamble.pop(0)
            preamble.append(num)
        else:
            print(f'First number with property: {num}')
            break
# Part 2
with open('input.txt', 'r') as f:
    sequence = [int(l.strip()) for l in f]

def indices_of_sum(num: int, seq: List[int]) -> Tuple[int, int]:
    for first in range(len(sequence)):
        s = sequence[first]
        for last in range(first + 1, len(sequence)):
            s += sequence[last]
            if s == num:
                return first, last
            if s > num:
                break
    return -1, -1

idx = indices_of_sum(num, sequence)
seq = sequence[idx[0]:idx[1] +1]
mx = max(seq)
mn = min(seq)
print(f'Min: {mn}, Max: {mx} = {mn + mx}')
