from collections import deque
import sys
sys.path.append('..')
from utils.io import read_input  # noqa


def parse_content(content: deque):
    # current = content.pop()
    # folder = current.split('$ cd ')[1]
    files = {}
    while True:
        if not len(content):
            print('empty')
            print(content)
            return {}
        current = content.pop()
        if '$ cd' in current:
            folder = current.split('$ cd ')[1]
            sub_structure = parse_content(content)
            files[folder] = sub_structure
            return {folder: files}
        elif '..' in current:
            return {folder: files}
        elif not 'dir ' in current and not '$ ls ':
            size, file = current.split()
            files[file] = int(size)


def parse(path):
    return (
        x for x in [[y.strip() for y in x.split('\n') if y and '$' not in y]
                    for x in ''.join(
            cmd for cmd in open(path).readlines() if '..' not in cmd
        ).split('$ cd')] if x)


def build_tree(ops): return {
    y[1]: build_tree(ops) if y[0] == 'dir' else int(y[0])
    for y in [x.split() for x in next(ops)[1:]]
}


def solve(tree, part):
    def flat(k): return (y for x in k for y in (
        flat(x) if type(x) is list else (x,)))

    def size(d): return sum(
        [v if type(v) is int else size(v) for v in d.values()])
    def vals(d): return [size(d), [vals(x)
                                   for x in [x for x in d.values() if type(x) is dict]]]
    return part(list(flat(vals(tree))))


def part_one(sizes):
    return sum(filter(lambda x: x < 100000, sizes))


def part_two(sizes):
    return min(filter(lambda x: x > 30000000 - (70000000 - max(sizes)), sizes))


# def solve():
#     content = read_input('7', 'input.txt')[0]
#     parsed_content = parse(content)
#     tree = build_tree(parsed_content)


if __name__ == "__main__":
    content = deque(read_input('7', 'input.txt'))
    content.reverse()
    parsed_content = parse_content(content)
    print(parsed_content)
    # parsed = parse('./input.txt')
    # print(list(parsed))
    # tree = build_tree(parsed)
    # print()
    # print(tree)
    # print('part 1:', solve(tree, part_one))
    # print('part 2:', solve(tree, part_two))
