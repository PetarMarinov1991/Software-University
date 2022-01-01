def josephus(prisoners, skip):
    idx = 0
    result = []
    while len(prisoners) > 0:
        idx = (idx + skip - 1) % len(prisoners)
        result.append((prisoners.pop(idx)))
    return result


def trim_white_spaces(elements):
    return '[' + ','.join(elements) + ']'


elements_list = input().split()
k = int(input())

print((trim_white_spaces(josephus(elements_list, k))))
