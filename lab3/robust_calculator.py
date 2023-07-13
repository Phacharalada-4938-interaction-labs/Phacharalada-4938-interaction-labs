def robust_calculator(op1, op2, operator, output_format):

    if not isinstance(op1, (float, int)) or not isinstance(op2, (float, int)):
        raise ValueError('Invalid operands. Operands must be numbers.')

    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Operator must be +, -, *, or /")

    if operator == "+":
        result = op1 + op2
    elif operator == "-":
        result = op1 - op2
    elif operator == "*":
        result = op1 * op2
    elif operator == "/":
        result = op1 / op2

    if output_format == "float":
        result = float(result)
    elif output_format == "int":
        result = round(result)

    return result


def get_operand(message):
    operand = input(message)
    if operand.lower() == "q":
        exit()
    try:
        return float(operand)
    except ValueError:
        raise ValueError("Invalid operand. Operand must be a number.")


def get_operator():
    operator = input("Enter an operation ('+', '-', '*', or '/'):")
    if operator.lower() == "q":
        exit()
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Operator must be +, -, *, or /")
    return operator


def get_format():
    format_input = input("Enter an output format (float, int):")
    if format_input.lower() == "q":
        exit()


def calculator():
    while True:
        try:
            op1 = get_operand("Enter the first operand ('q' to quit):")
            op2 = get_operand("Enter the second operand ('q' to quit):")
            operator = get_operator()
            requested_format = get_format()
            if op2 == 0:
                EE = '1'
            if requested_format not in ["int", "float"]:
                EE = '2'

            if EE == '1':
                print("Cannot divide by zero")
            elif EE == '2':
                print("Cannot divide by zero")
                print("We cannot perform your requested calculation")
            else:
                output = robust_calculator(op1, op2, operator, requested_format)
                print("{} {} {} = {:.1f}".format(op1, operator, op2, output))

        except ValueError as e:
            print("Error:", str(e))


if __name__ == "__main__":
    calculator()
