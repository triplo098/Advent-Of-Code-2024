def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    print(data)

    sum = 0
    start = 0

    while (1):

        index = data.find('mul(', start)

        # print(index)
        if index == -1:
            break

        start = index + 4

        word = data[start : start + 8]
        # print(word)

        colon_idx = word.find(',')
        bracket_idx = word.find(')')

        # print("c: ", colon_idx, "b: ", bracket_idx)

        if colon_idx >= bracket_idx:
            continue

        d_1 = word[0 : colon_idx]
        d_2 = word[colon_idx  + 1: bracket_idx]

        # print("d_1: ", d_1, "d_2: ", d_2)

        if d_1.isnumeric() and d_2.isnumeric():
            sum += int(d_1) * int(d_2)
        else:
            continue

    print(sum)

if __name__ == "__main__":
    main()
