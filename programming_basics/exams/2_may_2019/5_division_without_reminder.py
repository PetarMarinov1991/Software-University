n = int(input())

divided_by_2 = 0
divided_by_3 = 0
divided_by_4 = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        divided_by_2 += 1
    if number % 3 == 0:
        divided_by_3 += 1
    if number % 4 == 0:
        divided_by_4 += 1

p1 = divided_by_2 / n * 100
p2 = divided_by_3 / n * 100
p3 = divided_by_4 / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
