from typing import Dict, List


def parse_bag(bag: str) -> str:
    b = bag.split()
    if len(b) == 4:
        return '_'.join(b[1:3])
    else:
        return ''
        

def parse_line(line: str) -> Dict[str, List[str]]:
    [outer, inner] = [b.strip() for b in line.strip('.\n').split('contain')]
    o = outer.split()
    outer_bag = '_'.join(o[:2])
    inner_bags: List['str'] = list()
    if ',' in inner:
        bags = [i.strip() for i in inner.split(',')]
        for bag in bags:
            pb = parse_bag(bag)
            if pb:
                inner_bags.append(pb)
    else:
        pb = parse_bag(inner)
        if pb:
            inner_bags.append(pb)
    return {outer_bag: inner_bags}

        
all_bags: Dict[str, List[str]] = dict()
with open('input.txt', 'r') as f:
    for line in f:
        all_bags.update(parse_line(line))

def find(bag: str, in_bag: str, bag_map: Dict[str, List[str]]) -> bool:
    if in_bag not in bag_map:
        return False
    return bag in bag_map[in_bag] or any(
        [find(bag, b, bag_map) for b in bag_map[in_bag]]
    )

count = 0
for bag in all_bags:
    if find('shiny_gold', bag, all_bags):
        count += 1

print(f'Part 1 count: {count}')

# Part 2
def parse_bag_with_count(bag: str) -> Dict[str, int]:
    b = bag.split()
    if len(b) == 4:
        return {'_'.join(b[1:3]): int(b[0])}
    else:
        return dict()


def parse_with_count(line: str) -> Dict[str, Dict[str, int]]:
    [outer, inner] = [b.strip() for b in line.strip('.\n').split('contain')]
    o = outer.split()
    outer_bag = '_'.join(o[:2])
    inner_bags: Dict[str, int] = dict()
    if ',' in inner:
        bags = [i.strip() for i in inner.split(',')]
        for bag in bags:
            pbc = parse_bag_with_count(bag)
            if pbc:
                inner_bags.update(pbc)
    else:
        pbc = parse_bag_with_count(inner)
        if pbc:
            inner_bags.update(pbc)
    return {outer_bag: inner_bags}


counted_bags: Dict[str, Dict[str, int]] = dict()
with open('input.txt', 'r') as f:
    for line in f:
        counted_bags.update(parse_with_count(line))


def count_inner_bags(bag: str, bag_map: Dict[str, Dict[str, int]]) -> int:
    count = 0
    if bag not in bag_map:
        return 0
    for inner in bag_map[bag]:
        if not bag_map[inner]:
            count += bag_map[bag][inner]
        else:
            count += bag_map[bag][inner] + (
                bag_map[bag][inner] * count_inner_bags(inner, bag_map)
            )
    return count

shiny_bag_count = count_inner_bags('shiny_gold', counted_bags)
print(f'Part 2 count: {shiny_bag_count}')
