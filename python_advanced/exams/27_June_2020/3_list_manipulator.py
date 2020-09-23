def list_manipulator(*args):
    sequence = args[0]
    first_command, second_command = args[1], args[2]
    nums = None

    if len(args) > 2:
        nums = list(args[3:])

    if first_command == 'add':
        if second_command == 'beginning':
            sequence = nums + sequence
        elif second_command == 'end':
            sequence = sequence + nums
    elif first_command == 'remove':
        if second_command == 'beginning':
            if not nums:
                sequence = sequence[1:]
            else:
                sequence = sequence[nums[0]:]
        elif second_command == 'end':
            if not nums:
                sequence = sequence[:-1]
            else:
                sequence = sequence[:len(sequence) - nums[0]]
    return sequence
