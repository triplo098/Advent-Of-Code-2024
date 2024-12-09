from collections import OrderedDict

def push_to_free(k, v, word):

    temp_word = word[:]
    valid_index = -1

    for i, d in enumerate(temp_word):

        if d != '.':
            continue

        free_space = temp_word[i:i + v]

        if all(p == '.' for p in free_space):
            valid_index = i
            break

    if valid_index == -1 or valid_index >=word.index(k):
        pass
    else:
        word[word.index(k) : word.index(k) + v] = ['.' for k in range(v)]
        word[valid_index : valid_index + v] = [k for l in range(v)]

    return word


def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()
    data = data.replace('\n', '')
    disk_map = list(map(int, list(data)))

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

    files = dict()
    for i in set(word):
        if i == '.':
            continue
        files[int(i)] = word.count(i)

    files = {k: files[k] for k in sorted(files.keys(), reverse=False)}
    files_ordered = OrderedDict(sorted(files.items(), reverse=True))

    for key, value in files_ordered.items():
        word = push_to_free(str(key), value, word)

    print(''.join(word))

    index = -1
    s = 0

    for d in word:
        index += 1
        if d == '.':
            continue
        s += index * int(d)

    print(s)


if __name__ == "__main__":
    main()
