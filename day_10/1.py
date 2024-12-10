import queue

grid = []

def bsf_search(starting_position):
    global grid
    q = queue.Queue()
    pos_out = []
    count = 0
    q.put(starting_position)

    while not q.empty():
        pos = q.get()

        if grid[pos[0]][pos[1]] == 9 and [pos[0], pos[1]] not in pos_out:
            count += 1
            pos_out.append([pos[0], pos[1]])
            continue

        positions = get_adjecent_positions(pos)

        for p in positions:
            q.put(p)

    return count

def get_adjecent_positions(pos):
    global grid

    out_pos = []
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    v = grid[pos[0]][pos[1]]

    for p in directions:

        i = pos[0] + p[0]
        j = pos[1] + p[1]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue

        v_new = grid[i][j]
        if  v_new - v == 1:
            out_pos.append([i, j])

    return out_pos

def main():
    global grid
    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    grid = [[int(x) for x in row] for row in filter(None, data.split("\n"))]

    out = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                out += bsf_search([i, j])

    print(out)

if __name__ == "__main__":
    main()
