def josephus(numbers, k):
    idx = 0
    result = []
    while len(numbers) > 0:
        idx = (idx + k - 1) % len(numbers)
        result.append((numbers.pop(idx)))
    return result


def trim_white_spaces(elements):
    return '[' + ','.join(elements) + ']'


numbers = input().split()
k = int(input())

print((trim_white_spaces(josephus(numbers, k))))
