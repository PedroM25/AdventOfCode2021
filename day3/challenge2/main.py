def main():
    with open("../input.txt", "r") as f:
        all_lines = [line1.removesuffix("\n") for line1 in f.readlines()]

    num_columns = len(all_lines[0])

    # for o2
    curr_oxygen_lines = all_lines
    for i in range(num_columns+1):

        if len(curr_oxygen_lines) == 1:
            break

        zeros = 0
        ones = 0
        for line in curr_oxygen_lines:
            if line[i] == "0":
                zeros += 1
            if line[i] == "1":
                ones += 1

        curr_oxygen_winner = "1" if ones >= zeros else "0"

        tmp = []
        for line in curr_oxygen_lines:
            if line[i] == curr_oxygen_winner:
                tmp.append(line)
        curr_oxygen_lines = tmp

    # for co2
    curr_co2_lines = all_lines
    for i in range(num_columns+1):

        if len(curr_co2_lines) == 1:
            break

        zeros = 0
        ones = 0
        for line in curr_co2_lines:
            if line[i] == "0":
                zeros += 1
            if line[i] == "1":
                ones += 1

        curr_co2_winner = "0" if ones >= zeros else "1"

        tmp = []
        for line in curr_co2_lines:
            if line[i] == curr_co2_winner:
                tmp.append(line)
        curr_co2_lines = tmp

    return int(curr_oxygen_lines[0], 2) * int(curr_co2_lines[0], 2)


if __name__ == "__main__":
    print(main())
