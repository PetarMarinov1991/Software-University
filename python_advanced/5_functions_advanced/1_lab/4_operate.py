def operate(operator, *numbers):
    def get_initial_value(sign):
        if sign in ('+', '-'):
            return 0
        return 1

    result = get_initial_value(operator)

    for x in numbers:
        if operator == '+':
            result += x
        elif operator == '-':
            result -= x
        elif operator == '*':
            result *= x
        elif operator == '/':
            result /= x
    return result
