from test.support import swap_item

def main():

    readInput = False #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    data = data.replace('\n', '')
    disk_map = list(map(int, list(data)))

    # disk_map = disk_map[0:30]
    print(disk_map)

    ids_spaces = []
    free_spaces = []

    for en_i, d in enumerate(disk_map):
        if en_i % 2 == 0:
            ids_spaces.append(d)
        else:
            free_spaces.append(d)

    ids = [x for x in range(len(ids_spaces))]

    ids_spaces = ids_spaces[::-1]
    print(ids_spaces)
    print(free_spaces)
    print(ids)

    final_ids = [ids[0]]

    for i, id_s in enumerate(ids_spaces):

        for j, f_s in enumerate(free_spaces):
            if f_s >= id_s:
                free_spaces[j] = f_s - id_s

                ids = ids[0: j + 1] + ids[j+1:][-1:]+ ids[j+1:][:-1]

                print(ids)
                break


    # print(word)
    word = ""

    print(''.join(word))

    index = -1
    s = 0

    for d in word:

        index += 1
        if d == '.':
            continue

        print('i: ', index, 'd: ', d)

        s += index * int(d)

    print(s)


# 6505400213735 too high

if __name__ == "__main__":
    main()
