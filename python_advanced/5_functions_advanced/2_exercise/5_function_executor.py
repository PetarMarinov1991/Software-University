def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for i in range(len(args)):
        function = args[i][0]
        numbers = args[i][1]
        result.append(function(*numbers))
    return result
