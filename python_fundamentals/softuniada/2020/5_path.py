import itertools


def generator(combination):
    yield from itertools.product(*([combination] * stars))


path = input()

stars = 0
for ch in path:
    if ch == '*':
        stars += 1

combinations = []
count = 0
for comb in generator('LRS'):
    combinations.append([x for x in comb])
    count += 1

for combo in combinations:
    for idx in range(len(path)):
        if not path[idx] == '*':
            combo.insert(idx, path[idx])

print(count)
for combo in combinations:
    print(''.join(combo))
