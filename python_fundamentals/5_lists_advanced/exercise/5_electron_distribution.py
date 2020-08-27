n = int(input())

electrons = []

for i in range(n):
    formula = 2 * (i + 1) ** 2
    diff = n - sum(electrons)

    if diff == 0:
        break
    elif diff > formula:
        electrons.append(formula)
    else:
        electrons.append(diff)

print(electrons)
