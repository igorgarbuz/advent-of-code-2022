from collections import deque
import sys
sys.path.append('..')
from utils.io import read_input  # noqa


def solve():
    content = read_input('6', 'input.txt')[0]
    t = 14
    for i in range(len(content) - 1):
        win = content[i:i + t]
        unique = set(win)
        if len(unique) == t:
            return i + t

    return 0


if __name__ == "__main__":
    solution = solve()
    print(solution)
