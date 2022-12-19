import numpy as np


def part_1():
    with open("day_4/input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        pair_1, pair_2 = line.strip().split(",")
        num_1, num_2 = pair_1.split("-")
        num_3, num_4 = pair_2.split("-")
        range_1 = set(range(int(num_1), int(num_2) + 1))
        range_2 = set(range(int(num_3), int(num_4) + 1))

        sum += range_1 <= range_2 or range_2 <= range_1

    print(sum)


def part_2():
    with open("day_4/input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        pair_1, pair_2 = line.strip().split(",")
        num_1, num_2 = pair_1.split("-")
        num_3, num_4 = pair_2.split("-")
        range_1 = set(range(int(num_1), int(num_2) + 1))
        range_2 = set(range(int(num_3), int(num_4) + 1))

        sum += bool(range_1.intersection(range_2))

    print(sum)


if __name__ == "__main__":
    part_1()
    part_2()
