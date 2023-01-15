from copy import deepcopy
from collections import deque
import sys
sys.path.append('..')
from utils.io import read_input  # noqa # noqa indicates that this import cannot be reordered

START = (20, 0)

END = (20, 136)


def read_content() -> list[list[str]]:
    content = read_input('12', 'input.txt')
    content_coords = [list(x) for x in content]
    return content_coords


def build_vert_dic(ord_content):
    vert_list = {}
    for i, line in enumerate(ord_content):
        for j, val in enumerate(line):
            vert_list[(i, j)] = {'coord': (i, j), 'val': ord(val), 'color': 'WHITE',
                                 'distance': float('inf'), 'predecessor': None}
    return vert_list


def get_adj(vert_coords: list[int, int]):
    i, j = vert_coords
    return ((i+1, j), (i, j+1), (i-1, j), (i, j-1))


def solve():
    ord_content = read_content()
    # sanity check
    print('start char:', ord_content[START[0]][START[1]])
    print('end char:', ord_content[END[0]][END[1]])
    vert_dic = build_vert_dic(ord_content)
    queue = deque()
    start = vert_dic[START]
    start['distance'] = 0
    start['color'] = 'GREY'
    start['val'] = ord('a')  # go to any direction from start is possible
    end = vert_dic[END]
    end['val'] = ord('z')
    # sanity check
    print('start node:', vert_dic[START])
    print('end node:', vert_dic[END])
    queue.append(start)
    # print(start['coord'] == START)
    end_node = vert_dic[END]
    print('end reachable', end_node['coord'] == END)
    while len(queue) > 0:
        # print(len(queue))
        current_node = queue.pop()
        adj_nodes_coord = get_adj(current_node['coord'])
        # print('adj_node_coord', adj_nodes_coord)
        for node_coord in adj_nodes_coord:
            adj_node = vert_dic.get(node_coord)
            # print('adj_node', adj_node)
            # if not visited
            if adj_node and adj_node['color'] == 'WHITE':
                # exit condition -- reached end node
                if adj_node['coord'] == END:
                    return current_node['distance'] + 1
                # if reachable from the current note
                if adj_node['val'] <= current_node['val'] + 1:
                    adj_node['color'] = 'GREY'
                    adj_node['distance'] = current_node['distance'] + 1
                    adj_node['predecessor'] = current_node
                    # update FILO queue for BFS
                    queue.appendleft(adj_node)
        # set current node is behind expansion line and in the path
        current_node['color'] = 'BLACK'
    # print('vert_dic', vert_dic)
    return -1


def shortest_path_from_start(vert_dic, start_coord):
    queue = deque()
    start = vert_dic[start_coord]
    start['distance'] = 0
    start['color'] = 'GREY'
    queue.append(start)
    while len(queue) > 0:
        current_node = queue.pop()
        adj_nodes_coord = get_adj(current_node['coord'])
        for node_coord in adj_nodes_coord:
            adj_node = vert_dic.get(node_coord)
            # if not visited
            if adj_node and adj_node['color'] == 'WHITE':
                # exit condition -- reached end node
                if adj_node['coord'] == END:
                    return current_node['distance'] + 1
                # if reachable from the current note
                if adj_node['val'] <= current_node['val'] + 1:
                    adj_node['color'] = 'GREY'
                    adj_node['distance'] = current_node['distance'] + 1
                    # adj_node['predecessor'] = current_node
                    # update FILO queue for BFS
                    queue.appendleft(adj_node)
        # set current node is behind expansion line and in the path
        current_node['color'] = 'BLACK'
    return float('inf')


def solve_part_two():
    ord_content = read_content()
    # sanity check
    print('start char:', ord_content[START[0]][START[1]])
    print('end char:', ord_content[END[0]][END[1]])
    vert_dic = build_vert_dic(ord_content)
    # go to any direction from start is possible
    vert_dic[START]['val'] = ord('a')
    # go to any direction from start is possible
    vert_dic[END]['val'] = ord('z')
    all_a = [x['coord'] for x in vert_dic.values() if x['val'] == ord('a')]
    min_steps = float('inf')
    for idx, coord_a in enumerate(all_a):
        print(f'idx {idx} / {len(all_a)}')
        # print('coord_a', coord_a)
        # for coord_a in [START]:
        steps = shortest_path_from_start(deepcopy(vert_dic), coord_a)
        if coord_a == START:
            print('steps from start', steps)
        if steps < min_steps:
            min_steps = steps
    return min_steps


if __name__ == "__main__":
    # steps = solve()
    # print('\nsteps', steps)
    # Here bad solution for part two
    # elegant way to solve it is start from the end and go backwards
    # recursively updating distance from the end to all starting nodes
    steps_part_two = solve_part_two()
    print('\nsteps', steps_part_two)
