def check_contain(start, end, start_second, end_second):
    if start >= start_second and end <= end_second:
        return True
    if start_second >= start and end_second <= end:
        return True
    return False


def check_overlap(start, end, start_second, end_second):
    if start >= start_second and start <= end_second:
        return True
    if end >= start_second and end <= end_second:
        return True
    if start_second >= start and start_second <= end:
        return True
    if end_second >= start and end_second <= end:
        return True
    return False


def solve():
    input = '/Users/igorgarbuz/Documents/advent_of_code_2022/4/input.txt'
    f = open(input, 'r')
    content = f.read()
    f.close()
    content_split = content.split('\n')[:-1]
    score = 0
    for line in content_split:
        first, second = line.split(',')
        start_first, end_first = first.split('-')
        start_second, end_second = second.split('-')
        if check_contain(int(start_first), int(end_first), int(start_second), int(end_second)):
            score += 1
    return score


def solve_part_two():
    input = '/Users/igorgarbuz/Documents/advent_of_code_2022/4/input.txt'
    f = open(input, 'r')
    content = f.read()
    f.close()
    content_split = content.split('\n')[:-1]
    score = 0
    for line in content_split:
        first, second = line.split(',')
        start_first, end_first = first.split('-')
        start_second, end_second = second.split('-')
        if check_overlap(int(start_first), int(end_first), int(start_second), int(end_second)):
            score += 1
    return score


if __name__ == "__main__":
    # solution = solve()
    solution = solve_part_two()
    print(solution)
