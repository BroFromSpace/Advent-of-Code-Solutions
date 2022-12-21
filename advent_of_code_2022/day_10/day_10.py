from typing import List


def calc_strength(cycle: int, register: int, list_of_strength: List[int]):
    if cycle <= 220 and (cycle - 20) % 40 == 0:
        list_of_strength.append(cycle * register)


def draw_pixel(cycle: int, crt: List[List[str]], sprite_pos: List[int]):
    pos_y = cycle // 40
    cycle -= 40 * pos_y
    pos_x = cycle

    if cycle in sprite_pos:
        crt[pos_y][pos_x] = "#"


def part_1():
    with open("advent_of_code_2022/day_10/input.txt", "r") as f:
        lines = f.readlines()

    list_of_strength = []
    register = 1
    cycle = 0
    for line in lines:
        command = line.split()

        match command[0]:
            case "noop":
                cycle += 1
                calc_strength(cycle, register, list_of_strength)
            case "addx":
                cycle += 1
                calc_strength(cycle, register, list_of_strength)

                cycle += 1
                register += int(command[1])
                calc_strength(cycle, register, list_of_strength)

    print(sum(list_of_strength))


def part_2():
    with open("advent_of_code_2022/day_10/input.txt", "r") as f:
        lines = f.readlines()

    cycle = 0
    register = 1
    crt = [list(" "*40) for _ in range(6)]
    sprite_pos = [register - 1, register, register + 1]

    for line in lines:
        command = line.split()

        match command[0]:
            case "noop":
                cycle += 1
                draw_pixel(cycle, crt, sprite_pos)
            case "addx":
                cycle += 1
                draw_pixel(cycle, crt, sprite_pos)

                cycle += 1
                register += int(command[1])
                sprite_pos = [register - 1, register, register + 1]
                draw_pixel(cycle, crt, sprite_pos)

    for row in crt:
        for col in row:
            print(col, end="")

        print("")


if __name__ == "__main__":
    part_1()
    part_2()
