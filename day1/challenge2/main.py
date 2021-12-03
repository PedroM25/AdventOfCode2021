def main():
    print("Hello World!")
    print(calc())


def calc():
    prev_sum = 0
    no_increases = 0
    with open("../input.txt", "r") as f:
        l = f.readlines()
        prev_sum += int(l[0]) + int(l[1]) + int(l[2])
        try:
            for i in range(1, len(l)):
                current_sum = 0
                for j in range(i, i+3):
                    current_sum += int(l[j])
                if current_sum > prev_sum:
                    no_increases += 1
                prev_sum = current_sum
        except(IndexError):
            print("Index error")
        finally:
            return no_increases


if __name__ == "__main__":
    main()
