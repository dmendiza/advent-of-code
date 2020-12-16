from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Number:
    value: int
    last: int = -1
    previous: int = -1

starting_numbers = [int(n) for n in "16,12,1,0,15,7,11".split(',')]
turn: int
numbers: Dict[int, Number] = dict()
last_number: Number
first_time_spoken = True

for t, number in enumerate(starting_numbers):
    turn = t + 1  # turns start at 1
    n = Number(value=number)
    n.last = turn
    numbers[number] = n

# for turn in range(turn + 1, 2021):  Part 1
for turn in range(turn + 1, 30000001):  # Part 2
    if first_time_spoken:
        next_number = 0
    else:
        next_number = last_number.last - last_number.previous
    if next_number in numbers:
        first_time_spoken = False
        last_number = numbers[next_number]
    else:
        first_time_spoken = True
        last_number = Number(value=next_number)
        numbers[next_number] = last_number
    last_number.last, last_number.previous = turn, last_number.last

print(f'Last number spoken: {last_number.value}')
