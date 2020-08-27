def combinations(names, chairs, combos=[]):
    if len(combos) == chairs:
        print(', '.join(combos))
        return
    for i in range(len(names)):
        name = names[i]
        combos.append(name)
        combinations(names[i + 1:], chairs)
        combos.pop()


combinations(input().split(', '), int(input()))
