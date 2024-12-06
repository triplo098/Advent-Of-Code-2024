dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
dirs_keys = ['<', '^', '>', 'v']

#  1747 too high
def get_direction(orientation_char):
    d = dirs[dirs_keys.index(orientation_char)]
    return d

def turn_90_right(d):
    d_out = dirs[(dirs.index(d) + 1) % len(dirs)]
    return d_out

def perform_walking(grid, max_steps):

    pos = []
    for row in grid:
        for el in row:
            if el != '.' and el != '#' and el != 'X' and el != 'O':
               pos = [grid.index(row), row.index(el)]

    d = get_direction(grid[pos[0]][pos[1]])
    grid[pos[0]][pos[1]] = 'X'
    x_pos = []
    steps = 0

    while pos[0] + d[0] >= 0 and pos[0] + d[0] < len(grid) and pos[1] + d[1] >= 0 and pos[1] + d[1] < len(grid[0]):
        c = grid[pos[0] + d[0]][pos[1] + d[1]]
        if c == '#' or c == 'O':
           d = turn_90_right(d)
           continue

        pos = [pos[0] + d[0], pos[1] + d[1]]
        steps += 1
        if grid[pos[0]][pos[1]] != 'X':
            grid[pos[0]][pos[1]] = 'X'
            x_pos.append([pos[0], pos[1]])

        if steps > max_steps:
            for row in grid:
                print(str(row))

            print(" --- ")
            break

    return steps, x_pos


def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()


    grid = [list(line) for line in filter(None,data.split("\n"))]
    base_grid = [row[:] for row in grid]

    MAX = pow(len(base_grid), 2)
    my_sum = 0

    max_steps, x_pos = perform_walking(grid, MAX)
    print(max_steps)
    for x_p in x_pos:

        temp_grid = [row[:] for row in base_grid]
        temp_grid[x_p[0]][x_p[1]] = 'O'
        steps = perform_walking(temp_grid, MAX)[0]

        if steps > MAX:
            my_sum += 1

    print(my_sum)

if __name__ == "__main__":
    main()
