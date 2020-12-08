from typing import Any, List, Tuple


instructions: List[List[Any]] = list()

with open('input.txt', 'r') as f:
    for line in f:
        inst, val = line.strip().split()
        instructions.append([0, inst, val])

idx = 0
acc = 0

while idx < len(instructions):
    executed = instructions[idx][0]
    inst = instructions[idx][1]
    val = instructions[idx][2]
    if executed:
        break
    instructions[idx][0] = 1
    if inst == 'nop':
        idx += 1
        continue
    elif inst == 'acc':
        v = int(val[1:])
        if val.startswith('+'):
            acc += v
        elif val.startswith('-'):
            acc -= v
        idx += 1
        continue
    elif inst == 'jmp':
        v = int(val[1:])
        if val.startswith('+'):
            idx += v
        elif val.startswith('-'):
            idx -= v

print(f'Day 8 - Part 1 acc={acc}')

# Part 2
def execute(flip: int, instructions: List[List[Any]]) -> Tuple[bool, int]:
    idx = 0
    acc = 0
    aborted = False

    while idx < len(instructions):
        executed = instructions[idx][0]
        inst = instructions[idx][1]
        val = instructions[idx][2]
        if executed:
            aborted = True
            break
        if idx == flip:
            if inst == 'nop':
                inst = 'jmp'
            elif inst == 'jmp':
                inst = 'nop'
            else:
                raise ValueError()
        instructions[idx][0] = 1
        if inst == 'nop':
            idx += 1
            continue
        elif inst == 'acc':
            v = int(val[1:])
            if val.startswith('+'):
                acc += v
            elif val.startswith('-'):
                acc -= v
            idx += 1
            continue
        elif inst == 'jmp':
            v = int(val[1:])
            if val.startswith('+'):
                idx += v
            elif val.startswith('-'):
                idx -= v

    return aborted, acc

def reset(instructions: List[List[Any]]) -> None:
    for i in range(len(instructions)):
        instructions[i][0] = 0


def indices(op: str, instructions: List[List[Any]]) -> List[int]:
    idxs: List[int] = list()
    for i in range(len(instructions)):
        if instructions[i][1] == op:
            idxs.append(i)
    return idxs


nop_idx = indices('nop', instructions)
for idx in nop_idx:
    reset(instructions)
    result = execute(idx, instructions)
    if not result[0]:
        print(f'Part 2 acc: {result[1]}')
        break

jmp_idx = indices('jmp', instructions)
for idx in jmp_idx:
    reset(instructions)
    result = execute(idx, instructions)
    if not result[0]:
        print(f'Part 2 acc: {result[1]}')
