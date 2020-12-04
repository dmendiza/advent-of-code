from typing import Dict

_REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]


def validate_passport(passport: Dict[str, str]) -> bool:
    for field in _REQUIRED_FIELDS:
        if field not in passport.keys():
            return False
    return True


passport: Dict[str, str] = dict()
valid_passports = 0

with open('input.txt', 'r') as f:
    for line in f:
        fields = line.split()
        if not fields:
            if validate_passport(passport):
                valid_passports += 1
            passport = dict()
        else:
            for field in fields:
                k, v = field.split(':')
                passport[k] = v
    if validate_passport(passport):
        valid_passports += 1

print(f'Part 1: Valid passports: {valid_passports}')


# Part 2
class FieldValidator:
    def _validate_year(self, year: str, lowest: int, highest: int) -> bool:
        if len(year) != 4:
            return False
        try:
            y = int(year)
        except ValueError:
            return False
        return y >= lowest and y <= highest

    def byr(self, year: str) -> bool:
        return self._validate_year(year, 1920, 2002)

    def iyr(self, year: str) -> bool:
        return self._validate_year(year, 2010, 2020)

    def eyr(self, year: str) -> bool:
        return self._validate_year(year, 2020, 2030)

    def _validate_height(self, height: str, lowest: int, highest: int) -> bool:
        try:
            h = int(height)
        except ValueError:
            return False
        return h >= lowest and h <= highest

    def hgt(self, height: str) -> bool:
        if height.endswith('cm'):
            return self._validate_height(height[:-2], 150, 193)
        if height.endswith('in'):
            return self._validate_height(height[:-2], 59, 76)
        return False

    def hcl(self, color: str) -> bool:
        if not color.startswith('#'):
            return False
        if len(color) != 7:
            return False
        for c in color[1:]:
            if c not in '0123456789abcdef':
                return False
        return True

    def ecl(self, color: str) -> bool:
        return color in [
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
        ]

    def pid(self, passport_id: str) -> bool:
        if len(passport_id) != 9:
            return False
        try:
            int(passport_id)
        except ValueError:
            return False
        return True

def validate_passport2(passport: Dict[str, str]) -> bool:
    validator = FieldValidator()
    for field in _REQUIRED_FIELDS:
        if field not in passport.keys():
            return False
        if not getattr(validator, field)(passport[field]):
            return False
    return True

passport = dict()
valid_passports = 0

with open('input.txt', 'r') as f:
    for line in f:
        fields = line.split()
        if not fields:
            if validate_passport2(passport):
                valid_passports += 1
            passport = dict()
        else:
            for field in fields:
                k, v = field.split(':')
                passport[k] = v
    if validate_passport(passport):
        valid_passports += 1

print(f'Part 2: Valid passports: {valid_passports}')
