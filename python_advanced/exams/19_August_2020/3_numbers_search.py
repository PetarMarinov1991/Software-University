def numbers_searching(*args):
    repeating_values = [num for num in args if args.count(num) > 1]
    full_sequence = [x for x in range(min(args), max(args) + 1)]
    for num in full_sequence:
        if num not in args:
            return [num, sorted(set(repeating_values))]
