
def main():

    readInput = False #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    data = data.replace('\n', '')
    disk_map = list(map(int, list(data)))

    # print(disk_map)

    word = []
    idx = 0
    for en_i, d in enumerate(disk_map):
        if en_i % 2 == 0:
            for i in range(d):
                word.append(str(idx))
            idx += 1
        else:
            for i in range(d):
                word += '.'

    print(word)
    for i in range(len(word)):
        d = word[-1]
        del word[-1]

        if d == '.':
            continue

        id = word.index('.')
        word[id] = d

        try:
            id = word.index('.')
        except:
            break


    print(''.join(word))
    while '.' in word:
        word.remove('.')

    s = 0
    word_map = list(map(int, word))
    for i, d in enumerate(word_map):
        s += i * d

    print(s)

if __name__ == "__main__":
    main()
