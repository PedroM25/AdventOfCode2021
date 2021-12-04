def main():
    with open("../input.txt", "r") as f:
        all_lines = [line1.removesuffix("\n") for line1 in f.readlines()]
        num_columns = len(all_lines[0])

        zeros = [0] * num_columns
        ones = [0] * num_columns

        for line in all_lines:
            for i in range(num_columns):
                if line[i] == "0":
                    zeros[i] += 1
                elif line[i] == "1":
                    ones[i] += 1

        gamma_rate = [""] * num_columns
        epsilon_rate = [""] * num_columns
        for i in range(num_columns):
            if zeros[i] >= ones[i]:
                gamma_rate[i] = "0"
                epsilon_rate[i] = "1"
            else:
                gamma_rate[i] = "1"
                epsilon_rate[i] = "0"

        # power consumption
        return int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)


if __name__ == "__main__":
    print(main())
