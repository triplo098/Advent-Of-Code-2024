
def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    # print(data)

    left = []
    right = []

    for line in data.split("\n"):

        try:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))
        except:
            pass

    sum = 0
    for i in range(len(left)):

        min_l = min(left)
        min_r = min(right)
        left.remove(min_l)
        right.remove(min_r)

        diff = abs(min_l - min_r)
        sum += diff

    print(sum)

if __name__ == "__main__":
    main()
