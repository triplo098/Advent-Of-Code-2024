
def is_safe(report):
    is_dec = True
    is_asc = True

    for i in range(0, len(report) - 1):

        if report[i] < report[i + 1]:
            is_dec = False
        elif  report[i] > report[i + 1]:
            is_asc = False

        if (not is_dec )and (not is_asc):
            return False

        diff = abs(report[i] - report[i + 1])

        if diff > 3 or diff < 1:
            return False

    return True

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    data = list(filter(None, data.split("\n")))

    reports = [[int(i) for i in line.split(" ")] for line in data]

    sum = 0
    for report in reports:
        if is_safe(report):
            sum += 1

    print(sum)

if __name__ == "__main__":
    main()
