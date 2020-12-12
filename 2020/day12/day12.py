from dataclasses import dataclass
import math


@dataclass
class Vector:
    x: int
    y: int

_DIRECTION_TO_DEG = {
    "E": 0,
    "N": 90,
    "W": 180,
    "S": 270
}

_DEG_TO_DIRECTION = {
    0: "E",
    90: "N",
    180: "W",
    270: "S"
}

_DIRECTION_VECTOR = {
    "E": Vector(1, 0),
    "N": Vector(0, 1),
    "W": Vector(-1, 0),
    "S": Vector(0, -1)
}


def move(current: Vector, direction: str, value: int) -> Vector:
    dirv = _DIRECTION_VECTOR[direction]
    return Vector(
        current.x + (dirv.x * value),
        current.y + (dirv.y * value)
    )


def rotate(current: str, deg: int) -> str:
    cur = _DIRECTION_TO_DEG[current]
    return _DEG_TO_DIRECTION[(cur + deg) % 360]


facing = "E"
position = Vector(0, 0)

with open('input.txt', 'r') as f:
    for line in f:
        l = line.strip()
        action = l[0]
        value = int(l[1:])
        if action in "NSEW":
            position = move(position, action, value)
        if action == 'F':
            position = move(position, facing, value)
        if action == 'L':
            facing = rotate(facing, value)
        if action == 'R':
            facing = rotate(facing, -value)

manhattan = abs(position.x) + abs(position.y)
print(f'Part 1 - Manhattan distance: {manhattan}')


# Part 2
def move_to_waypoint(pos: Vector, times: int, waypoint: Vector) -> Vector:
    return Vector(
        pos.x + (waypoint.x * times),
        pos.y + (waypoint.y * times)
    )


def rotate_waypoint(waypoint: Vector, deg: int) -> Vector:
    return Vector(
        int(round(
            waypoint.x * math.cos(math.radians(deg)) -
            waypoint.y * math.sin(math.radians(deg))
        )),
        int(round(
            waypoint.x * math.sin(math.radians(deg)) +
            waypoint.y * math.cos(math.radians(deg))
        ))
    )

waypoint = Vector(10, 1)
ship = Vector(0, 0)

with open('input.txt', 'r') as f:
    for line in f:
        l = line.strip()
        action = l[0]
        value = int(l[1:])
        if action in "NSEW":
            waypoint = move(waypoint, action, value)
        if action == "F":
            ship = move_to_waypoint(ship, value, waypoint)
        if action == "L":
            waypoint = rotate_waypoint(waypoint, value)
        if action == "R":
            waypoint = rotate_waypoint(waypoint, -value)

manhattan = abs(ship.x) + abs(ship.y)
print(f'Part 2 - Manhattan distance: {manhattan}')

