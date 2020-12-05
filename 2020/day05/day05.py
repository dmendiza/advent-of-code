def to_row_id(row: str) -> int:
    ids = [0, 127]
    for i in range(6):
        fe = (ids[1] - ids[0]) // 2
        if row[i] == 'F':
            ids = [ids[0], ids[0] + fe]
        elif row[i] == 'B':
            ids = [ids[0] + fe + 1, ids[1]]
        else:
            raise ValueError()
    return row[-1] == 'F' and ids[0] or ids[1]

def to_column_id(column: str) -> int:
    ids = [0, 7]
    for i in range(2):
        half = (ids[1] - ids[0]) // 2
        if column[i] == 'L':
            ids = [ids[0], ids[0] + half]
        elif column[i] == 'R':
            ids = [ids[0] + half + 1, ids[1]]
        else:
            raise ValueError()
    return column[-1] == 'L' and ids[0] or ids[1]

def to_seat_id(seat: str) -> int:
    return (to_row_id(seat[:-3]) * 8) + to_column_id(seat[-3:])


if __name__ == '__main__':
    highest = 0
    with open('input.txt', 'r') as f:
        for line in f:
            seat_id = to_seat_id(line.strip())
            if seat_id > highest:
                highest = seat_id
    print(f'Part 1: Highest seat ID {highest}')

    seat_map = [[0 for _ in range(8)] for _ in range(128)]
    with open('input.txt', 'r') as f:
        for line in f:
            row = to_row_id(line.strip()[:-3])
            col = to_column_id(line.strip()[-3:])
            seat_map[row][col] = 1

    for r in range(128):
        for c in range(8):
            if seat_map[r][c] == 0:
                seat_id = (r * 8) + c
                print(f'Missing seat row {r} column {c} ID {seat_id}')
    # Part 2 was dumb.  Had to inspect visually to find the correct answer

