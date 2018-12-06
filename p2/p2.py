# AOC -- https://adventofcode.com/2018/day/2
# Box Checksum
# Find the frequency of boxes with frequencies of letters, multiplied together

import os

AOC_DIR = 'C:\\Users\\mnowak6\\Desktop\\advent_of_code_2018'
PUZZLE_NAME = 'p2'
INPUT_FILENAME = 'input.txt'
INPUT_FILE = os.path.join(AOC_DIR, PUZZLE_NAME, INPUT_FILENAME)

def read_input(filename):
    with open(filename, 'r') as input_file:
        return input_file.read()

def parse(puzzle_lines):
    puzzle_lines = [pl.strip() for pl in puzzle_lines.split()]
    return puzzle_lines

def count_letter_frequency(puzzle_input):
    result = []
    for pl in puzzle_input:
        counts = {}
        for c in pl:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        result.append(counts)
    return result

def part_one(puzzle_input):
    count_dict = count_letter_frequency(puzzle_input)
    num_2 = len([c for c in count_dict if 2 in c.values()])
    num_3 = len([c for c in count_dict if 3 in c.values()])
    return num_2 * num_3

def get_similar_letters(p1, p2):
    return ''.join([cc[0] if cc[0] == cc[1] else '' for cc in zip(p1, p2)])

def part_two(puzzle_input):
    for p1 in puzzle_input:
        for p2 in puzzle_input:
            if sum([0 if cc[0] == cc[1] else 1 for cc in zip(p1, p2)]) == 1:
                return get_similar_letters(p1, p2)
    
    return False

if __name__ == "__main__":
    puzzle_input = parse(read_input(INPUT_FILE))

    print('Part 1', part_one(puzzle_input))
    print('Part 2', part_two(puzzle_input))
