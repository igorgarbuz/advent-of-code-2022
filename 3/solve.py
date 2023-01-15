def solve():
    input = '/Users/igorgarbuz/Documents/advent_of_code_2022/3/input.txt'
    f = open(input, 'r')
    content = f.read()
    f.close()
    content_split = content.split('\n')[:-1]
    letters = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()
    scores = {ch: idx + 1 for idx, ch in enumerate(letters)}
    print(scores)
    score = 0
    for line in content_split:
        half_line = len(line) // 2
        first_half = line[:half_line]
        second_half = line[half_line:]
        common_item = list(set(first_half).intersection(second_half))[0]
        score += scores[common_item]
    return score


def solve_part_two():
    input = '/Users/igorgarbuz/Documents/advent_of_code_2022/3/input.txt'
    f = open(input, 'r')
    content = f.read()
    f.close()
    content_split = content.split('\n')[:-1]
    letters = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()
    scores = {ch: idx + 1 for idx, ch in enumerate(letters)}
    score = 0
    group_size = 3
    n = 0
    for n in range(0, len(content_split), group_size):
        group = content_split[n:n + group_size]
        # print(group)
        # print()
        for ch in group[0]:
            if ch in group[1] and ch in group[2]:
                score += scores[ch]
                break

    return score


if __name__ == "__main__":
    # solution = solve()
    solution = solve_part_two()
    print(solution)
