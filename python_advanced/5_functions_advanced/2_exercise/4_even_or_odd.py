def even_odd(*args):
    numbers = [int(x) for x in args[:-1]]
    command = args[-1]
    if command == 'even':
        return [num for num in numbers if num % 2 == 0]
    return [num for num in numbers if num % 2 != 0]
