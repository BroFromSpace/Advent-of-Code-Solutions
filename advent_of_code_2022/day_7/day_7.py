def part_1():
    with  open("advent_of_code_2022/day_7/input.txt", "r") as f:
        lines = f.readlines()

    inputs = []
    sizes = {}

    for line in lines:
        line = line.replace("$ ", "")
        if line[0:2] != "ls" and line[0:3] != "dir":
            inputs.append(line)

    stack = []
    for i in range(len(inputs)):
        line = inputs[i]
        if line[0:2] == "cd" and ".." in line:
            stack.pop()
        elif line[0:2] == "cd":
            stack.append(i)
            sizes[i] = 0
        else:
            size = int(line.split()[0])
            for s in stack:
                sizes[s] += size

    result = sum([sizes[i] for i in sizes if sizes[i] <= 100000])
    print(result)


def part_2():
    with  open("advent_of_code_2022/day_7/input.txt", "r") as f:
        lines = f.readlines()

    inputs = []
    sizes = {}

    for line in lines:
        line = line.replace("$ ", "")
        if line[0:2] != "ls" and line[0:3] != "dir":
            inputs.append(line)

    stack = []
    for i in range(len(inputs)):
        line = inputs[i]
        if line[0:2] == "cd" and ".." in line:
            stack.pop()
        elif line[0:2] == "cd":
            stack.append(i)
            sizes[i] = 0
        else:
            size = int(line.split()[0])
            for s in stack:
                sizes[s] += size

    unused = 70000000 - sizes[0]
    unused_needed = 30000000 - unused
    potential_deletes = [sizes[i] for i in sizes if sizes[i] >= unused_needed]
    result = min(potential_deletes)
    print(result)


if __name__ == "__main__":
    part_1()
    part_2()
