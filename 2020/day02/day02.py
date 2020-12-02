from typing import List, NamedTuple


class _LetterRange(NamedTuple):
    lowest: int
    highest: int


class Policy:
    """Rental Place Down the Street Policy"""
    required_letter: str
    required_range: _LetterRange

    def __init__(self, from_str: str) -> None:
        range_str, self.required_letter = from_str.strip().split()
        [lowest, highest] = [int(x) for x in range_str.strip().split('-')]
        self.required_range = _LetterRange(lowest, highest)

    def is_valid(self, password: str) -> bool:
        ct = password.count(self.required_letter)
        return (ct >= self.required_range.lowest and
                ct <= self.required_range.highest)

class PolicyTwo:
    """Toboggan Corporate Policy"""
    required_letter: str
    positions: List[int]

    def __init__(self, from_str: str) -> None:
        pos_str, self.required_letter = from_str.strip().split()
        # we subtract 1 from given positions to use as 0-based index
        self.positions = [int(x) - 1 for x in pos_str.strip().split('-')]

    def is_valid(self, password: str) -> bool:
        in_first_pos = (password[self.positions[0]] == self.required_letter)
        in_second_pos = (password[self.positions[1]] == self.required_letter)
        return in_first_pos != in_second_pos



if __name__ == '__main__':
    print('Advent of Code 2020 - Day 2')
    count = 0
    count2 = 0
    with open('input.txt', 'r') as f:
        for line in f:
            l = line.strip('\n')
            p, pwd = l.split(': ')
            policy = Policy(p)
            if policy.is_valid(pwd):
                count += 1
            policy2 = PolicyTwo(p)
            if policy2.is_valid(pwd):
                count2 += 1
    print(f'Valid Rental Place Passwords {count}')
    print(f'Valid Toboggan Passwords {count2}')
