from itertools import permutations, combinations
import re
import code
import pprint
from collections import deque
import heapq
import sys
sys.path.append('..')
from utils.io import read_input  # noqa

pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

TEST_RESULT_1 = 1651
TEST_RESULT_2 = 1707


class Node:
    def __init__(self, rate, adjacent_valves):
        self.rate = rate
        self.adjacent_valves = adjacent_valves


def parse(content) -> dict[str, Node]:
    graph = {}
    for line in content:
        valve_id = line[6:8]
        rate = int(re.search(r'\d+', line).group())
        adjacent_valves = re.search(r'valves? (.*)', line).group(1).split(', ')
        graph[valve_id] = Node(rate, adjacent_valves)

    return graph


def all_pairs_shortest_path(graph: dict[str, Node]) -> dict[(str, str), int]:
    '''Floyd-Warshall algorithm'''
    # initialize distance matrix
    distance = {(i, j): float('inf') for i in graph for j in graph}
    for i in graph:
        distance[(i, i)] = 0
        for j in graph[i].adjacent_valves:
            distance[(i, j)] = 1
    for k, i, j in permutations(graph, 3):
        distance[(i, j)] = min(distance[(i, j)],
                               distance[(i, k)] + distance[(k, j)])
    return distance


def visit(current_id, remaining_time, total_potential_volume, rates, distances, paths_with_volumes, path):
    paths_with_volumes[tuple(path)] = max(paths_with_volumes.get(
        tuple(path), 0), total_potential_volume)
    for next_node_id, rate in rates:
        if next_node_id in path:
            continue
        distance = distances[(current_id, next_node_id)]
        # time to reach and open the next valve
        next_remaining_time = remaining_time - distance - 1
        if next_remaining_time <= 0:
            continue
        visit(next_node_id, next_remaining_time,
              total_potential_volume + rate * next_remaining_time, rates, distances, paths_with_volumes, path.union([next_node_id]))


def solve(content, time=30, agents=1):
    graph = parse(content)
    start = 'AA'
    total_volume = 0
    distances = all_pairs_shortest_path(graph)
    rates = sorted({id: node.rate for id, node in graph.items()
                   if node.rate > 0}.items(), key=lambda x: x[1], reverse=True)
    # starting from the node Start, initiate DFS, but allow revisiting node
    # and check if final volume is greater
    paths_with_volumes = {}
    visit(start, time, total_volume,
          rates, distances, paths_with_volumes, set())
    if agents == 1:
        return max(paths_with_volumes.values())
    elif agents == 2:
        def intersection(lst1, lst2):
            return len(set(lst1) & set(lst2)) > 0
        # find the best path for each agent
        return max([item1[1] + item2[1] for item1, item2 in combinations(
            paths_with_volumes.items(), 2) if not intersection(item1[0], item2[0])])


if __name__ == '__main__':
    content = read_input('16', 'input.txt')
    solution = solve(content)
    print('part1', solution)
    solution = solve(content, 26, 2)
    print('part2', solution)
