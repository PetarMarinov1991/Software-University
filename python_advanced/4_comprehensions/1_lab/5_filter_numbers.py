print(list(sorted(set(
    [x for x in [int(x) for x in range(int(input()), int(input()) + 1)]
     for num in [x for x in range(2, 11)]
     if x % num == 0]))))
