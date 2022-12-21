from typing import List, Tuple

import numpy as np


def move_rope(head: Tuple[int, int], tail: Tuple[int, int], direction: str):
    match direction:
        case "R":
            head_movement = [0, 1]
        case "L":
            head_movement = [0, -1]
        case "U":
            head_movement = [-1, 0]
        case "D":
            head_movement = [1, 0]

    head = np.add(head, head_movement)

    diff = np.subtract(head, tail)
    if np.linalg.norm(diff) > np.sqrt(2):
        tail_movement = [1 if i != 0 else 0 for i in diff]
        tail_movement = np.sign(diff) * tail_movement
        tail = np.add(tail, tail_movement)
    return head, tail


def move_long_rope(pos_list: List[List[Tuple[int, int]]], direction: str):
    match direction:
        case "R":
            head_movement = [0, 1]
        case "L":
            head_movement = [0, -1]
        case "U":
            head_movement = [-1, 0]
        case "D":
            head_movement = [1, 0]

    pos_list[0].append(np.add(pos_list[0][-1], head_movement))

    for i, j in enumerate(pos_list):
        if i != 9:
            head, tail = j[-1], pos_list[i+1][-1]
            diff = np.subtract(head, tail)
            if np.linalg.norm(diff) > np.sqrt(2):
                tail_movement = [1 if i != 0 else 0 for i in diff]
                tail_movement = np.sign(diff) * tail_movement
                tail = np.add(tail, tail_movement)
            pos_list[i+1].append(tail)
    return pos_list


def part_1():
    with open("advent_of_code_2022/day_9/input.txt", "r") as f:
        lines = f.readlines()

    tail_pos = []
    head, tail = (0, 0), (0, 0)
    tail_pos.append([0, 0])
    for i in lines:
        direction, num = i.split()
        num = int(num)
        for i in range(num):
            head, tail = move_rope(head, tail, direction)
            tail_pos.append(tail)

    print(np.unique(np.asarray(tail_pos), axis=0).shape[0])



def part_2():
    with open("advent_of_code_2022/day_9/input.txt", "r") as f:
        lines = f.readlines()

    pos_list = [[(0, 0)] for i in range(10)]

    for line in lines:
        direction, num = line.split()
        num = int(num)
        for i in range(num):
            pos_list = move_long_rope(pos_list, direction)

    print(np.unique(np.asarray(pos_list[-1]), axis=0).shape[0])


if __name__ == "__main__":
    part_1()
    part_2()
