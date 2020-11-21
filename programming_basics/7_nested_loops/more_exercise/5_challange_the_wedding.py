men_count = int(input())
women_count = int(input())
tables = int(input())

pair = 0

for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        pair += 1
        if not pair > tables:
            print(f'({men} <-> {women})', end=' ')
