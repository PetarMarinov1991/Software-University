number = int(input())

total = 0

for num in range(0, number):
    next_num = int(input())
    total += next_num

average = total / number
print(f'{average:.2f}')
