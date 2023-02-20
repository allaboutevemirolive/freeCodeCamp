def arithmetic_arranger(problems, answer=False):
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Create lists for first operands, second operands, and operators
    operands1 = []
    operands2 = []
    operators = []

    # Loop through each problem and split into pieces, adding first and second operands and operator to their respective lists
    for problem in problems:
        pieces = problem.split()
        operands1.append(pieces[0])
        operators.append(pieces[1])
        operands2.append(pieces[2])

    # Check if operator is valid (+ or -)
    if "*" in operators or "/" in operators:
        return "Error: Operator must be '+' or '-'."

    # Check if operands are valid (contain only digits)
    for i in range(len(operands1)):
        if not (operands1[i].isdigit() and operands2[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check if operands are valid (not more than 4 digits)
    for i in range(len(operands1)):
        if len(operands1[i]) > 4 or len(operands2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Create lists for each line of the arranged problems
    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    # Loop through each problem and add formatted first operand to first line list
    for i in range(len(operands1)):
        if len(operands1[i]) > len(operands2[i]):
            top_line.append(" " * 2 + operands1[i])
        else:
            top_line.append(" " * (len(operands2[i]) - len(operands1[i]) + 2) + operands1[i])

    # Loop through each problem and add formatted second operand with operator to second line list
    for i in range(len(operands2)):
        if len(operands2[i]) > len(operands1[i]):
            bottom_line.append(operators[i] + " " + operands2[i])
        else:
            bottom_line.append(operators[i] + " " * (len(operands1[i]) - len(operands2[i]) + 1) + operands2[i])

    # Loop through each problem and add dashes to third line list
    for i in range(len(operands1)):
        dash_line.append("-" * (max(len(operands1[i]), len(operands2[i])) + 2))

    # If answer is True, add formatted answers to fourth line list
    if answer:
        for i in range(len(operands1)):
            if operators[i] == "+":
                ans = str(int(operands1[i]) + int(operands2[i]))
            else:
                ans = str(int(operands1[i]) - int(operands2[i]))

            if len(ans) > max(len(operands1[i]), len(operands2[i])):
                answer_line.append(" " + ans)
            else: 
                answer_line.append(" " * (max(len(operands1[i]), len(operands2[i])) - len(ans) + 2) + ans)

        # Join all four lines into a single string with four spaces between each problem
        arranged_problems = "    ".join(top_line) + "\n" + "    ".join(bottom_line) + "\n" + "    ".join(dash_line) + "\n" + "    ".join(answer_line)
    else:
        # Join the first three lines into a single string with four spaces between each problem
        arranged_problems = "    ".join(top_line) + "\n" + "    ".join(bottom_line) + "\n" + "    ".join(dash_line)

    # Return the final output string
    return arranged_problems