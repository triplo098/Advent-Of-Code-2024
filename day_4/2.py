from itertools import product
import numpy as np


def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()
    print(data)

    matrix = [[c for c in line] for line in list(filter(None, data.split("\n") ))]

    a = np.array(matrix)

    print(a.shape)


    print(matrix)
    sum = 0


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            c = matrix[i][j]

            if c == 'A':

                # print("i ", i, "j ", j)
                if i < 1 or j < 1 or i >= len(matrix) - 1 or j >= len(matrix[0]) - 1:
                    break

                diag_1 = {matrix[i - 1][j - 1], matrix[i + 1][j + 1]}
                diag_2 = {matrix[i - 1][j + 1], matrix[i + 1][j - 1]}

                # print(diag_1)
                # print(diag_2)
                ms = {'M', 'S'}

                if ms == diag_1 and ms == diag_2:
                    sum += 1
                    # print("MAS")


    print(sum)



if __name__ == "__main__":
    main()
