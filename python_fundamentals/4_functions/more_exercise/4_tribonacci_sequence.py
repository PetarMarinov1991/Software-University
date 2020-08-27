def sequence(a, b, c):
    start = [a, b, c]
    result = []
    for _ in range(int(input())):
        start.append(sum(start))
        result.append(start.pop(0))

    print(*result)


sequence(a=1, b=1, c=2)
