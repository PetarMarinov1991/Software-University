def fix_calendar(numbers):
    while True:
        swap = False
        for i in range(len(numbers)):
            if i + 1 in range(len(numbers)) and numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap = True
        if swap:
            continue
        return numbers
