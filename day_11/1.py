import numpy as np

def blink(stones):
    # for i in np.nditer(x, op_flags = ['readwrite']):
    #     i[...] = 1
    stones_out = []
    for i, s in enumerate(stones):

        to_append = []
        if s == 0:
            to_append = [1]
        elif len(str(s)) % 2 == 0:
            num = str(s)
            to_append = [int(num[:len(num) // 2]), int(num[len(num) // 2:])]
        else:
            to_append = [s * 2024]

        stones_out += to_append

    return stones_out

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    # print(data)
    # stones = np.array([int(x) for x in data.split(" ")])

    stones = [int(x) for x in filter(None, data.split(" "))]

    for i in range(75):
        stones = blink(stones)

    print(len(stones))




if __name__ == "__main__":
    main()
