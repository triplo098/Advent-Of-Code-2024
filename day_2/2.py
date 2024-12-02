def is_dec(r):
    for i in range(0, len(r) - 1):
        if r[i] < r[i + 1]:
            return False
    return True

def is_asc(r):
    for i in range(0, len(r) - 1):
        if r[i] > r[i + 1]:
            return False
    return True

def diff_valid(r):
    for i in range(0, len(r) - 1):
        diff = abs(r[i] - r[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(report):

    dec = True
    asc = True

    for i in range(0, len(report)):

        report_removed = report.copy()
        report_removed.pop(i)

        dec = is_dec(report) or is_dec(report_removed)
        asc = is_asc(report) or is_asc(report_removed)
        diff = diff_valid(report) or diff_valid(report_removed)

        # print("d", dec, "a", asc, "diff", diff)

        if (dec or asc) and diff:
            return True

    return False

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
