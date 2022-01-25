from random import randint
from typing import Tuple

from numpy import argsort


def create_file():
    """Create a file with random numbers

    Create a file with 3 random numbers per line and 100 lines.

    """

    # open file to write numbers
    with open('./files/random_numbers.txt', 'w') as file:
        for _ in range(100):
            # create list of 3 random numbers
            l_rand = [str(randint(0, 10)) for __ in range(3)]

            # write random numbers into file
            file.write(' '.join(l_rand) + '\n')


def get_lines_and_keys() -> Tuple[str, int]:
    """Calculate key per line

    The key is defined as the sum of the line entries.

    :returns: tuple with lines of random numbers and related keys (aka sum of lines)
    """
    with open('./files/random_numbers.txt', 'r') as file:
        # store lines in list
        lines = file.read().splitlines()
        # calculate sum of lines
        keys = list(map(_get_line_sum, lines))

    return lines, keys


def write_sorted_list():
    """Sort lines by keys and write lines into file"""
    # get lines and key per line (key is the sum of entries per line)
    lines, keys = get_lines_and_keys()

    # sort key values
    sorted_indexes = argsort(keys).tolist()

    with open('./files/random_numbers_key_sorted.txt', 'w') as file:
        file.write('\n'.join([f'{str(keys[s_k])}: {lines[s_k]}' for s_k in reversed(sorted_indexes)]))


def get_max_and_min_key() -> Tuple[int, int]:
    """Get minimum and maximum key"""
    # get lines and key per line (key is the sum of entries per line)
    _, keys = get_lines_and_keys()

    return min(keys), max(keys)


def _get_line_sum(line: str) -> int:
    """Calculate sum of numbers stored in a string"""
    # split string list and convert entries to integer values and calculate sum of it
    return sum(list(map(int, (line.split(' ')))))
