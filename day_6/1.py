dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
dirs_keys = ['<', '^', '>', 'v']

def get_direction(orientation_char):
    d = dirs[dirs_keys.index(orientation_char)]
    return d

def turn_90_right(d):
    d_out = dirs[(dirs.index(d) + 1) % len(dirs)]
    return d_out

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    print(data)

    grid = [list(line) for line in filter(None,data.split("\n"))]

    pos = []

    for row in grid:
        for el in row:
            if el != '.' and el != '#' and el != 'X':
               pos = [grid.index(row), row.index(el)]

    d = get_direction(grid[pos[0]][pos[1]])
    grid[pos[0]][pos[1]] = 'X'

    while pos[0] + d[0] >= 0 and pos[0] + d[0] < len(grid) and pos[1] + d[1] >= 0 and pos[1] + d[1] < len(grid[0]):

        if grid[pos[0] + d[0]][pos[1] + d[1]] == '#':
           d = turn_90_right(d)
           continue

        pos = [pos[0] + d[0], pos[1] + d[1]]
        grid[pos[0]][pos[1]] = 'X'

    my_sum = sum([row.count('X') for row in grid])

    print(my_sum)

    # for row in grid:
    #     print(str(row))

if __name__ == "__main__":
    main()
