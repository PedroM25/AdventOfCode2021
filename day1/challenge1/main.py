def main():
    print("Hello World!")
    print(calc())


def calc():
    prev_depth = 0
    no_increases = 0
    with open("day1\challenge1\input.txt", "r") as f:
        l = f.readlines()
        prev_depth = int(l[0])
        for i in range(1,len(l)):
            curr_depth = int(l[i])
            if curr_depth > prev_depth:
                no_increases += 1
            prev_depth = curr_depth
    return no_increases


if __name__ == "__main__":
    main()
