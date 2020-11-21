stadium_capacity = int(input())
fans = int(input())

A = 0
B = 0
V = 0
G = 0

for fan in range(fans):
    sector = input()
    if sector == 'A':
        A += 1
    elif sector == 'B':
        B += 1
    elif sector == 'V':
        V += 1
    elif sector == 'G':
        G += 1

percentage_A = A / fans * 100
percentage_B = B / fans * 100
percentage_V = V / fans * 100
percentage_G = G / fans * 100
average = fans / stadium_capacity * 100

print(f'{percentage_A:.2f}%')
print(f'{percentage_B:.2f}%')
print(f'{percentage_V:.2f}%')
print(f'{percentage_G:.2f}%')
print(f'{average:.2f}%')
