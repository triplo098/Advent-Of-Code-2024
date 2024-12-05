rules = []

def is_valid(visited):

    global rules
    for page in visited:

        applied_rules = [rule for rule in rules if rule[0] == page]

        for rule in applied_rules:

            if rule[1] in visited and visited.index(page) > visited.index(rule[1]):
                return False

    return True

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read().split("\n\n")

    global rules

    rules = [list(map(int, i.split("|"))) for i in data[0].split("\n")]
    updates = [list(map(int, i.split(","))) for i in filter(None, data[1].split("\n"))]

    sum = 0

    for update in updates:
        visited = update[:]

        valid = is_valid(visited)

        if not valid:

            while (not is_valid(visited)):

                for page in visited:

                    applied_rules = [rule for rule in rules if rule[0] == page]

                    for rule in applied_rules:

                        i_page = visited.index(page)

                        if rule[1] not in visited:
                            continue

                        i_sec = visited.index(rule[1])

                        if i_page > i_sec:
                            # print("swapped")
                            visited[i_page], visited[i_sec] = visited[i_sec], visited[i_page]

            sum += visited[(len(visited) // 2)]

    print(sum)

if __name__ == "__main__":
    main()
