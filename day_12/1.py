from queue import Queue


def get_n_pos(pos):
    global grid

    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    n = []
    for dir in dirs:

        i = pos[0] + dir[0]
        j = pos[1] + dir[1]

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue

        if grid[pos[0]][pos[1]] == grid[i][j]:
            n.append([i, j])

    return n

def main():
    global grid
    readInput = False #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    grid = [[x for x in row] for row in filter(None, data.split("\n"))]
    print(grid)

    regions = dict()

    for i, row in enumerate(grid):
        for j, x in enumerate(row):

            if x not in regions.keys():
                regions[x] = [[i, j]]

            for r_i in range(len(regions[x])):
                if [i, j] in regions[x][r_i]:
                    continue
                else:
                    regions[x][r_i].append([i, j])


                region = regions[x][r_i][:]
                positions = Queue()
                positions.put([i, j])

                while positions.not_empty:
                    pos = positions.get()
                    # print("pos ", pos)
                    # print("region: ", region)

                    n = get_n_pos(pos)
                    n = [x for x in n if x not in region]
                    # print("n: ", n)
                    if len(n) == 0:
                        break
                    for p in n:

                        # print(p)
                        if p in region:
                            continue

                        region.append(p)
                        positions.put(p)


                print(f"region {x} {r_i} -> {region}")



if __name__ == "__main__":
    main()
