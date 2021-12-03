def main():
    print(calc())


def calc():
    hor_pos = 0
    final_depth = 0
    aim = 0
    with open("../input.txt", "r") as f:
        for line in f:
            line_split = line.removesuffix("\n").split(" ")
            val = int(line_split[1])
            if line_split[0] == "forward":
                hor_pos += val
                final_depth += aim * val
            elif line_split[0] == "down":
                aim += val
            elif line_split[0] == "up":
                aim -= val
    return hor_pos * final_depth

if __name__ == "__main__":
    main()
