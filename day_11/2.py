import numpy as np

def blink_rec(stones, n):

    out_num = 0

    if n == 1:
        return len(stones)

    print(n)
    for stone in stones:

        if stone == 0:
            out_num += blink_rec([1], n - 1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            out_num += blink_rec([int(s[:len(s) // 2]), int(s[len(s) // 2:])], n - 1)
        else:
            out_num += blink_rec([stone*2024], n -1)

    return out_num


def main():

    readInput = False #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    # print(data)
    # stones = np.array([int(x) for x in data.split(" ")])

    stones = [int(x) for x in filter(None, data.split(" "))]

    out = blink_rec(stones, 75)

    print(out)




if __name__ == "__main__":
    main()
