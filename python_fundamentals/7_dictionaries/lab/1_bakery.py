elements = input().split()
bakery = dict()

for i in range(0, len(elements), 2):
    k, v = elements[i], elements[i + 1]
    bakery[k] = int(v)

print(bakery)
