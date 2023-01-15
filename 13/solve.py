from collections import deque
from functools import cmp_to_key
import json
import sys
sys.path.append('..')
from utils.io import read_input  # noqa # noqa indicates that this import cannot be reordered


def compare(l, r):
    for left, right in zip(l, r):
        if type(left) == int and type(right) == int:
            res = left - right
        else:
            right = [right] if type(right) == int else right
            left = [left] if type(left) == int else left
            res = compare(left, right)
        if res != 0:
            return res
    return len(l) - len(r)


def solve():
    pairs_str = read_input('13', 'input.txt', '\n\n')
    pairs = []
    for pair in pairs_str:
        left, right = pair.split('\n')
        pairs.append((json.loads(left), json.loads(right)))
    valid = []
    for idx, pair in enumerate(pairs, 1):
        if compare(pair[0], pair[1]) < 0:
            valid.append(idx)
    return sum(valid)


def solve_part_two():
    pairs_str = read_input('13', 'input.txt', '\n\n')
    pairs = []
    for pair in pairs_str:
        left, right = pair.split('\n')
        pairs.append((json.loads(left), json.loads(right)))
    packets = sorted([packet for pair in pairs for packet in pair] +
                     [[[2]], [[6]]], key=cmp_to_key(compare))

    out_idx = 1
    for idx, packet in enumerate(packets, 1):
        if packet in ([[2]], [[6]]):
            out_idx *= idx

    return out_idx


if __name__ == "__main__":
    # sum_idx = solve()
    # print('\nsum_idx', sum_idx)
    prod_idx = solve_part_two()
    print('\solve_part_two', prod_idx)
