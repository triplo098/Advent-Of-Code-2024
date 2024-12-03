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
    enabled = True

    while (1):

        do_index = data.find('do()', start)
        dont_index = data.find('don\'t()', start)
        mul_index = data.find('mul(', start)

        # print(do_index, dont_index, mul_index)

        if mul_index == -1:
            break

        if (mul_index < do_index and mul_index < dont_index) or (do_index == -1 and dont_index == -1):
            start = mul_index + 4
        elif do_index < dont_index or (dont_index == -1 and do_index != -1):
            enabled = True
            start = do_index + 4
        elif do_index > dont_index or (do_index == -1 and dont_index != -1):
            enabled = False
            start = dont_index + 6

        if enabled == False:
            continue

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

    print(sum)

if __name__ == "__main__":
    main()
