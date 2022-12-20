def part_1():
    with open("advent_of_code_2022/day_6/input.txt", "r") as f:
        buffer = f.readlines()[0]

    result_index = 0
    for i in range(len(buffer)):
        if len(set(buffer[i:i+4])) == 4:
            result_index = i+4
            break

    print(result_index)


def part_2():
    with open("advent_of_code_2022/day_6/input.txt", "r") as f:
        buffer = f.readlines()[0]

    result_index = 0
    for i in range(len(buffer)):
        if len(set(buffer[i:i+14])) == 14:
            result_index = i+14
            break

    print(result_index)


if __name__ == "__main__":
    part_1()
    part_2()
