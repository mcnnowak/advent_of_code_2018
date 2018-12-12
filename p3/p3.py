# AOC -- https://adventofcode.com/2018/day/3
# Overlapping Rectangles of Fabric
# Find the sum of the overlapping 1x1in squares of cloth.

import os, re

AOC_DIR = 'C:\\Users\\mnowak6\\Desktop\\advent_of_code_2018'
PUZZLE_NAME = 'p3'
INPUT_FILENAME = 'input.txt'
INPUT_FILE = os.path.join(AOC_DIR, PUZZLE_NAME, INPUT_FILENAME)

INPUT_REGEX = '#(?P<case>\d+)\s+@\s+(?P<cx>\d+),(?P<cy>\d+):\s+(?P<dx>\d+)x(?P<dy>\d+)'
INPUT_REGEX_KEYS = 'case', 'cx', 'cy', 'dx', 'dy'


def read_input(filename):
    with open(filename, 'r') as input_file:
        return input_file.read()

def parse(puzzle_input):
    keys = INPUT_REGEX_KEYS
    puzzle_lines = [pl.strip() for pl in puzzle_input.split('\n')]    
    return [{k: int(v) for k, v in zip(keys, re.match(INPUT_REGEX, line).group(*keys))} for line in puzzle_lines]

def intersect(r1, r2):
    right = min(r1.get('cx') + r1.get('dx'), r2.get('cx') + r2.get('dx'))
    left = max(r1.get('cx'), r2.get('cx'))

    top = min(r1.get('cy') + r1.get('dy'), r2.get('cy') + r2.get('dy'))
    bottom = max(r1.get('cy'), r2.get('cy'))

    if right < left or top < bottom:
        return 0
    
    return (right - left) * (top - bottom)

if __name__ == "__main__":
    puzzle_input = parse(read_input(INPUT_FILE))

    points = set()
    dupes = set()

    # part 1
    for r in puzzle_input:
        for x in range(r.get('cx'), r.get('cx') + r.get('dx')):
            for y in range(r.get('cy'), r.get('cy') + r.get('dy')):
                point = tuple([x, y])
                if point in points:
                    dupes.add(point)
                else:
                    points.add(point)

    print(len(dupes))

    # part 2
    for r1 in puzzle_input:
        intersected = False
        for r2 in puzzle_input:
            if r1.get('case') == r2.get('case'):
                continue

            if intersect(r1, r2) > 0:
                intersected = True
                break

        if not intersected:
            print(r1.get('case'))
            break
