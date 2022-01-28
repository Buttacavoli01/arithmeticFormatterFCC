import re


def arithmetic_arranger(problems, solve=False):
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    # making sure there are no more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    for prob in problems:
        # searching to make sure only digits and the + and - operators are there
        if re.search("[^\s0-9.+-]", prob):
            if re.search("[/]", prob) or re.search("[*]", prob):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        num = prob.split(" ")[0]
        op = prob.split(" ")[1]
        num2 = prob.split(" ")[2]

        if len(num) >= 5 or len(num2) >= 5:
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if op == "+":
            sum = str(int(num) + int(num2))
        elif op == "-":
            sum = str(int(num) - int(num2))

        length = max(len(num), len(num2)) + 2
        top = str(num).rjust(length)
        bottom = op + str(num2).rjust(length - 1)
        res = str(sum).rjust(length)

        line = ""
        for j in range(length):
            line += '-'
        # adjusting for 4 spaces after each problem
        if prob != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines

    return string
