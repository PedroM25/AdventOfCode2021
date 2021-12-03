def main():
    print(calc())


def calc():
    hor_pos = 0
    final_depth = 0
    with open("../input.txt", "r") as f:
        for line in f.readlines():
            line_split = line.removesuffix("\n").split(" ")
            val = int(line_split[1])
            if line_split[0] == "forward":
                hor_pos += val
            elif line_split[0] == "down":
                final_depth += val
            elif line_split[0] == "up":
                final_depth -= val
    return hor_pos * final_depth

if __name__ == "__main__":
    main()
