# AOC -- https://adventofcode.com/2018/day/1
# Frequency Changes
# Sum the frequency changes.

import os

AOC_DIR = 'C:\\Users\\mnowak6\\Desktop\\advent_of_code_2018'
PUZZLE_NAME = 'p1'
INPUT_FILENAME = 'input.txt'
INPUT_FILE = os.path.join(AOC_DIR, PUZZLE_NAME, INPUT_FILENAME)

def read_input(filename):
    with open(filename, 'r') as input_file:
        return input_file.read()

def split_frequencies(puzzle_input):
    return puzzle_input.split()

def parse_frequencies(puzzle_input_list):
    return [int(freq) for freq in puzzle_input_list]

def sum_frequencies(frequencies):
    return sum(frequencies)

if __name__ == "__main__":
    puzzle_input = read_input(INPUT_FILE)
    split_frequency_sequence = split_frequencies(puzzle_input)
    parsed_frequency_sequence = parse_frequencies(split_frequency_sequence)
    print(sum_frequencies(parsed_frequency_sequence))
