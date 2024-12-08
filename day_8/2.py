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

            d_i = p[0][0] - p[1][0]
            d_j = p[0][1] - p[1][1]

            coords = [p[0][0] + d_i, p[0][1] + d_j]

            while is_in_boundry(coords, grid):
                grid[coords[0]][coords[1]] = '#'
                coords[0] += d_i
                coords[1] += d_j

            coords = p[0][:]

            while is_in_boundry(coords, grid):
                grid[coords[0]][coords[1]] = '#'
                coords[0] -= d_i
                coords[1] -= d_j

    for row in grid:
        print(str(row))

    print(sum([row.count('#') for row in grid]))


if __name__ == "__main__":
    main()
