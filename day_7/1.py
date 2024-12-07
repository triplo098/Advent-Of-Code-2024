import itertools


def operation(x, y, op_char):

    if op_char == '+':
        return x + y
    elif op_char == '*':
        return x * y

def main():

    readInput = True #deciding between demo or input

    if readInput == True:
        fileNameToRead = "input.txt"
    else:
        fileNameToRead = "demo_input.txt"

    data = open(fileNameToRead, "r").read()

    # print(data)
    equations = []
    for equation in filter(None, data.split("\n")):
        equations.append(list(map(int, equation.replace(": ", " ").split(" "))))

    operators = '+*'

    valid_sum = 0

    for equation in equations:
        exp_result = equation[0]
        x = 1
        for ops in itertools.product(operators, repeat=len(equation) - 2):

            eq = equation[:]
            for i, op in enumerate(ops):
                # print(f"{eq[i + 1]} {eq[i+2]} {op}")
                eq[i + 2] = operation(eq[i + 1], eq[i + 2], op)
                x = eq[i + 2]

            if x == exp_result:
                # print(x)
                valid_sum += x
                break

    print(valid_sum)
    # print(equations)



if __name__ == "__main__":
    main()
