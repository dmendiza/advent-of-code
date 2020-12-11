from typing import List, Tuple


def occupied_adjacent_seats(seat: Tuple[int, int], seatmap: List[str]) -> int:
    rows = len(seatmap)
    seats = len(seatmap[0])
    occupied = 0
    for row in range(-1, 2):
        if seat[0] + row < 0 or seat[0] + row >= rows:
            continue
        for col in range(-1, 2):
            if seat[1] + col < 0 or seat[1] + col >= seats:
                continue
            if row == 0 and col == 0:
                continue
            if seatmap[seat[0] + row][seat[1] + col] == '#':
                occupied += 1
    return occupied


def apply_rules(seatmap: List[str]) -> Tuple[int, List[str]]:
    seats_changed = 0
    new_seatmap = list()
    for r, row in enumerate(seatmap):
        new_row = ''
        for s, seat in enumerate(row):
            if seat == 'L' and occupied_adjacent_seats((r, s), seatmap) == 0:
                seats_changed += 1
                new_row += '#'
            elif seat == '#' and occupied_adjacent_seats((r, s), seatmap) >= 4:
                seats_changed += 1
                new_row += 'L'
            else:
                new_row += seat
        new_seatmap.append(new_row)
    return seats_changed, new_seatmap


def occupied(seatmap: List[str]) -> int:
    occ = 0
    for row in seatmap:
        for seat in row:
            if seat == '#':
                occ += 1
    return occ


with open('input.txt', 'r') as f:
    seatmap = [line.strip() for line in f]

changed, seatmap = apply_rules(seatmap)
while changed != 0:
    changed, seatmap = apply_rules(seatmap)

occ = occupied(seatmap)
print(f'Part 1 - Occupied: {occ}')

# Part 2
def is_occupied_looking_from(frm: Tuple[int, int], seatmap: List[str]) -> int:
    rows = len(seatmap)
    cols = len(seatmap[0])
    frm_row = frm[0]
    frm_col = frm[1]

    occ = 0

    # east
    row = seatmap[frm_row]
    for c in range(frm_col + 1, cols):
        if row[c] == '#':
            occ += 1
        if row[c] != '.':
            break
    # ne
    r = frm_row - 1
    c = frm_col + 1
    while r >= 0 and c < cols:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r -= 1
        c += 1

    # n
    r = frm_row - 1
    c = frm_col
    while r >= 0:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r -= 1

    # nw
    r = frm_row - 1
    c = frm_col - 1
    while r >= 0 and c >= 0:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r -= 1
        c -= 1

    # w
    r = frm_row
    c = frm_col - 1
    while c >= 0:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        c -= 1

    # sw
    r = frm_row + 1
    c = frm_col - 1
    while r < rows and c >= 0:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r += 1
        c -= 1

    # s
    r = frm_row + 1
    c = frm_col
    while r < rows:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r += 1

    # se
    r = frm_row + 1
    c = frm_col + 1
    while r < rows and c < cols:
        if seatmap[r][c] == '#':
            occ += 1
        if seatmap[r][c] != '.':
            break
        r += 1
        c += 1

    return occ


def apply_rules2(seatmap: List[str]) -> Tuple[int, List[str]]:
    seats_changed = 0
    new_seatmap = list()
    for r, row in enumerate(seatmap):
        new_row = ''
        for s, seat in enumerate(row):
            if seat == 'L' and is_occupied_looking_from((r, s), seatmap) == 0:
                seats_changed += 1
                new_row += '#'
            elif seat == '#' and is_occupied_looking_from((r, s), seatmap) >= 5:
                seats_changed += 1
                new_row += 'L'
            else:
                new_row += seat
        new_seatmap.append(new_row)
    return seats_changed, new_seatmap

with open('input.txt', 'r') as f:
    seatmap = [line.strip() for line in f]

changed, seatmap = apply_rules2(seatmap)

while changed != 0:
    changed, seatmap = apply_rules2(seatmap)

occ = occupied(seatmap)
print(f'Part 2 - Occupied: {occ}')
