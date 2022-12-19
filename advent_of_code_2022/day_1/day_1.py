def part_1():
    with open("advent_of_code_2022/day_1/input.txt", "r") as f:
        lines = f.readlines()

    # Go throw each line and find max kkals and current kkals
    cur_kk = 0
    max_kk = 0
    for line in lines:
        if line != "\n":
            cur_kk += int(line)
        else:
            if cur_kk > max_kk:
                max_kk = cur_kk
            cur_kk = 0

    print(max_kk)


def part_2():
    with open("advent_of_code_2022/day_1/input.txt", "r") as f:
        lines = f.readlines()

    # Go throw each line and find max kkals and current kkals
    arr = []
    cur_kk = 0
    max_kk = 0
    for line in lines:
        if line != "\n":
            cur_kk += int(line)
        else:
            if cur_kk > max_kk:
                max_kk = cur_kk

            arr.append(cur_kk)
            cur_kk = 0

    # Get sum of 3 biggest kkals items in list
    total_sum = sum(sorted(arr, reverse=True)[:3])

    print(total_sum)


if __name__ == "__main__":
    part_1()
    part_2()
