from collections import deque
import sys
sys.path.append('..')
from utils.io import read_input  # noqa

BINS = 9


def read_stacks(content):
    stacks = [deque() for _ in range(BINS)]
    T = 4
    n = 0
    for line in content:
        for i in range(BINS):
            box = line[i * T:(i + 1) * T].strip()
            if box:
                stacks[i].append(box[1])
    for stack in stacks:
        stack.reverse()
    return stacks


def read_moves(moves):
    moves_int = []
    for move in moves:
        move_digits = list(map(int, move.replace('move ', '').replace(
            'from ', '').replace('to ', '').split(' ')))
        moves_int.append(move_digits)
    return moves_int


def solve():
    content = read_input('5', 'input.txt')
    boxes, moves = content[:8], content[10:]
    stacks = read_stacks(boxes)
    moves = read_moves(moves)
    for move in moves:
        num, start, end = move
        for _ in range(num):
            stacks[end - 1].append(stacks[start - 1].pop())
    result = ''
    for stack in stacks:
        result += stack.pop()
    return result


def solve_part_two():
    content = read_input('5', 'input.txt')
    boxes, moves = content[:8], content[10:]
    stacks = read_stacks(boxes)
    moves = read_moves(moves)
    for move in moves:
        print(move)
        num, start, end = move
        tmp = []
        for _ in range(num):
            tmp.append(stacks[start - 1].pop())
        tmp.reverse()
        for box in tmp:
            stacks[end - 1].append(box)
    result = ''
    for stack in stacks:
        result += stack.pop()
    return result


if __name__ == "__main__":
    solution = solve()
    solution_two = solve_part_two()
    print(solution)
    print(solution_two)
