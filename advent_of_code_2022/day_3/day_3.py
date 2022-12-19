from functools import reduce
import numpy as np


def get_item_value(item: str):
    # Return value of item based on Unicode representation of character
    if item.islower():
        return ord(item) - 96

    return ord(item) - 38


def part_1():
    with open("day_3/input.txt", "r") as f:
        lines = f.readlines()

    # Map each line in lines with lambda function that splits rucksack
    # in 2 equal sets and find the same item with set intersection
    total_value = sum(map(lambda line: get_item_value(list(set(
        line[:int(len(line)/2)]).intersection(set(line[int(len(line)/2):])))[0]), lines))

    print(total_value)


def part_2():
    with open("day_3/input.txt", "r") as f:
        lines = np.array(f.readlines())

    # 1. Split all lines in groups for 3 lines in each group
    # 2. Map all groups and find the same item in each group with set intersection
    total_value = sum(map(lambda group: get_item_value(list(set(group[0].strip()).intersection(
        set(group[1].strip())).intersection(group[2].strip()))[0]), np.array_split(lines, len(lines)/3)))

    print(total_value)


if __name__ == "__main__":
    part_2()
