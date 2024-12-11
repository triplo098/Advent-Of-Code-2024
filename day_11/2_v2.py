import numpy as np
import math

def blink_rec(stones, n):

    out_num = 0

    if n == 1:
        return len(stones)

    print(n)
    for stone in stones:

        num_of_dig = math.floor(math.log(abs(stone), 10) + 1)

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

    stones = [int(x) for x in filter(None, data.split(" "))]

    out = blink_rec(stones, 75)






if __name__ == "__main__":
    main()
