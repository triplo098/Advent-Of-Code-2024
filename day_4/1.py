from itertools import product

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()
    print(data)

    matrix = [[c for c in line] for line in list(filter(None, data.split("\n") ))]

    print(matrix)
    sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            c = matrix[i][j]

            if c == 'X':

                base_directions = [-1, 0, 1] #    x, y
                directions = product(base_directions, repeat=2)

                for dir in directions:
                    if dir[0] == 0 and dir[1] == 0:
                        continue

                    new_i = i + dir[0]
                    new_j = j + dir[1]

                    print("dir: ", dir)
                    mas = ['M', 'A', 'S']
                    check = []
                    for l in mas:

                        # print("i ", i, "j ", j)
                        # print("new_i: ", new_i, "new_j: ", new_j)

                        if new_i < 0 or new_j < 0 or new_i >= len(matrix) or new_j >= len(matrix[0]):
                            break

                        selected_char = matrix[new_i][new_j]

                        # print("sc: ", selected_char)
                        # print("l: ", l)
                        if selected_char != l:
                            break

                        check.append(selected_char)
                        new_i += dir[0]
                        new_j += dir[1]

                    print("check: ", check)
                    if check == mas:
                        sum += 1

    print(sum)



if __name__ == "__main__":
    main()
