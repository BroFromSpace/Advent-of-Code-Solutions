def part_1():
    with open("day_2/input.txt", "r") as f:
        lines = f.readlines()

    # Create dictionary with all possible combinations
    points = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    # Map all combinations and replace them with combination value
    total_sum = sum(map(lambda line: points[line.strip()], lines))

    print(total_sum)


def part_2():
    with open("day_2/input.txt", "r") as f:
            with open("day_2/input.txt", "r") as f:
                lines = f.readlines()

    # Create dictionary with all possible combinations
    points = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    # Map all combinations and replace them with combination value
    total_sum = sum(map(lambda line: points[line.strip()], lines))

    print(total_sum)


if __name__ == "__main__":
    part_1()
    part_2()
