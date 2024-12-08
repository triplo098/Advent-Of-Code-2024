from itertools import combinations

def is_in_boundry(position, grid):

    i = position[0]
    j = position[1]

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False

    return True

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    grid = [list(line) for line in filter(None, data.split("\n"))]

    for row in grid:
        print(str(row))

    frequencies = dict()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):

            if c == '.':
                continue

            if c not in frequencies.keys():
                frequencies[c] = []

            frequencies[c].append([i, j])

    for pos in frequencies.values():
        permuts = combinations(pos, 2)

        for p in permuts:

            print(p)

            d_i = p[0][0] - p[1][0]
            d_j = p[0][1] - p[1][1]

            print(d_i, d_j)

            coords_1 = [p[0][0] + d_i, p[0][1] + d_j]
            coords_2 = [p[1][0] - d_i, p[1][1] - d_j]

            if is_in_boundry(coords_1, grid):
                grid[coords_1[0]][coords_1[1]] = '#'

            if is_in_boundry(coords_2, grid):
                grid[coords_2[0]][coords_2[1]] = '#'

    for row in grid:
        print(str(row))

    print(sum([row.count('#') for row in grid]))

if __name__ == "__main__":
    main()
