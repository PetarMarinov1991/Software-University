def combinations(combo, start, end):
    if start == end:
        print(''.join(combo))
    else:
        for i in range(start, end + 1):
            combo[start], combo[i] = combo[i], combo[start]
            combinations(combo, start + 1, end)
            combo[start], combo[i] = combo[i], combo[start]


string = input()
combinations(list(string), 0, len(string) - 1)
