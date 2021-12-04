def main():
    with open("../input.txt", "r") as f:
        all_lines = [line1.removesuffix("\n") for line1 in f.readlines()]

    num_columns = len(all_lines[0])

    # o2
    o2_lambda = lambda ones, zeros: "1" if ones >= zeros else "0"
    o2_rating = calculate_rating(all_lines, num_columns, o2_lambda)

    # co2
    co2_lambda = lambda ones, zeros: "0" if ones >= zeros else "1"
    co2_rating = calculate_rating(all_lines, num_columns, co2_lambda)

    return o2_rating * co2_rating


def calculate_rating(all_lines, num_columns, comparison):
    curr_lines = all_lines
    for i in range(num_columns + 1):

        if len(curr_lines) == 1:
            break

        zeros = 0
        ones = 0
        for line in curr_lines:
            if line[i] == "0":
                zeros += 1
            if line[i] == "1":
                ones += 1

        curr_winner = comparison(ones, zeros)

        tmp = []
        for line in curr_lines:
            if line[i] == curr_winner:
                tmp.append(line)
        curr_lines = tmp
    return int(curr_lines[0], 2)


if __name__ == "__main__":
    print(main())
