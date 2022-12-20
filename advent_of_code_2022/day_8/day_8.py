from typing import List


def is_visible(x_0: int, y_0: int, x_1: int, y_1: int, trees: List[List[int]]) -> bool:
    if x_1 < 0 or x_1 > 98 or y_1 < 0 or y_1 > 98:
        return True

    if trees[y_0][x_0] > trees[y_1][x_1]:
        if x_0 > x_1:
            return is_visible(x_0, y_0, x_1 - 1, y_1, trees)
        elif x_0 < x_1:
            return is_visible(x_0, y_0, x_1 + 1, y_1, trees)
        elif y_0 > y_1:
            return is_visible(x_0, y_0, x_1, y_1 - 1, trees)
        elif y_0 < y_1:
            return is_visible(x_0, y_0, x_1, y_1 + 1, trees)

    return False


def get_score(x_0: int, y_0: int, x_1: int, y_1: int, trees: List[List[int]]) -> int:
    if x_1 < 0 or x_1 > 98 or y_1 < 0 or y_1 > 98:
        return 0

    if trees[y_0][x_0] > trees[y_1][x_1]:
        if x_0 > x_1:
            return 1 + get_score(x_0, y_0, x_1 - 1, y_1, trees)
        elif x_0 < x_1:
            return 1 + get_score(x_0, y_0, x_1 + 1, y_1, trees)
        elif y_0 > y_1:
            return 1 + get_score(x_0, y_0, x_1, y_1 - 1, trees)
        elif y_0 < y_1:
            return 1 + get_score(x_0, y_0, x_1, y_1 + 1, trees)
    elif trees[y_0][x_0] == trees[y_1][x_1]:
        return 1

    return 0


def part_1():
    with open("advent_of_code_2022/day_8/input.txt", "r") as f:
        lines = f.readlines()

    results = []
    trees = list(map(lambda line: list(line.strip()), lines))
    for y in range(99):
        for x in range(99):
            results.append(any(
                (
                    is_visible(x, y, x - 1, y, trees),
                    is_visible(x, y, x + 1, y, trees),
                    is_visible(x, y, x, y - 1, trees),
                    is_visible(x, y, x, y + 1, trees)
                )
            ))

    print(sum(results))


def part_2():
    with open("advent_of_code_2022/day_8/input.txt", "r") as f:
        lines = f.readlines()

    results = []
    trees = list(map(lambda line: list(line.strip()), lines))
    for y in range(99):
        for x in range(99):
            results.append(
                get_score(x, y, x - 1, y, trees) *
                get_score(x, y, x + 1, y, trees) *
                get_score(x, y, x, y - 1, trees) *
                get_score(x, y, x, y + 1, trees)
            )

    print(max(results))


if __name__ == "__main__":
    part_1()
    part_2()
