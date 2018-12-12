# AOC -- https://adventofcode.com/2018/day/4
# Guard Sleep Patterns
# Find the guard ID of the guard that sleeps the most, multiplied by the minute
# on which that guard sleeps the most.

import os, re
from datetime import datetime

AOC_DIR = 'C:\\Users\\mnowak6\\Desktop\\advent_of_code_2018'
PUZZLE_NAME = 'p4'
INPUT_FILENAME = 'input.txt'
INPUT_FILE = os.path.join(AOC_DIR, PUZZLE_NAME, INPUT_FILENAME)

INPUT_REGEX = '\[(?P<datetimestring>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\].*'
INPUT_REGEX_DATE = 'datetimestring'


def read_input(filename):
    with open(filename, 'r') as input_file:
        return input_file.read()

def parse(puzzle_input):
    puzzle_lines = [pl.strip() for pl in puzzle_input.split('\n') if pl.strip()]
    return [(str_to_date(re.match(INPUT_REGEX, line).group(INPUT_REGEX_DATE)), line) for line in puzzle_lines]

def str_to_date(datestring):
    return datetime.strptime(datestring, '%Y-%m-%d %H:%M')

if __name__ == "__main__":
    puzzle_input = parse(read_input(INPUT_FILE))
    puzzle_input.sort(key=(lambda p: p[0]))

    guards = set()
    for line in puzzle_input:
        if '#' not in line[1]:
            continue
        
        guard_id = re.match('.*#(?P<guard>\d+).*', line[1]).group('guard')
        guards.add(int(guard_id))
        
    print(guards)
