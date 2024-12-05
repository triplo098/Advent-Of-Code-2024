def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    data = data.split("\n\n")

    rules = [list(map(int, i.split("|"))) for i in data[0].split("\n")]

    updates = [list(map(int, i.split(","))) for i in filter(None, data[1].split("\n"))]

    sum = 0

    for update in updates:
        visited = update[:]

        valid = True

        print("visited:", visited)

        for page in visited:

            applied_rules = [rule for rule in rules if rule[0] == page]

            print("page", page)
            print("ar", applied_rules)

            for rule in applied_rules:

                print(rule)

                if rule[1] in visited and visited.index(page) > visited.index(rule[1]):

                    print("NOT_VALID")

                    valid = False

        if valid:
            print("VALID")
            sum += update[(len(update) // 2)]
            print("sum += ", sum)

    print(sum)

if __name__ == "__main__":
    main()
