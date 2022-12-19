import re

stacks = [
    ["B", "P", "N", "Q", "H", "D", "R", "T"],
    ["W", "G", "B", "J", "T", "V"],
    ["N", "R", "H", "D", "S", "V", "M", "Q"],
    ["P", "Z", "N", "M", "C"],
    ["D", "Z", "B"],
    ["V", "C", "W", "Z"],
    ["G", "Z", "N", "C", "V", "Q", "L", "S"],
    ["L", "G", "J", "M", "D", "N", "V"],
    ["T", "P", "M", "F", "Z", "C", "G"]
]


def part_1():
    with open("day_5/input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        # For each line get move, from and to values
        move, from_, to = [int(s) for s in re.findall(r'\b\d+\b', line)]
        # Move numbers from stack 1 to stack 2
        # Reverse numbers as we need to put numbers in reverse way
        stacks[to-1].extend(stacks[from_-1][-move:][::-1])
        # Delete numbers from stack 1
        del stacks[from_-1][-move:]

    for stack in stacks:
        print(stack[-1], end="")


def part_2():
    with open("day_5/input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        # For each line get move, from and to values
        move, from_, to = [int(s) for s in re.findall(r'\b\d+\b', line)]
        # Move number from stack 1 to stack 2
        stacks[to-1].extend(stacks[from_-1][-move:])
        # Delete numbers from stack 1
        del stacks[from_-1][-move:]

    for stack in stacks:
        print(stack[-1], end="")


if __name__ == "__main__":
    part_1()
    part_2()
