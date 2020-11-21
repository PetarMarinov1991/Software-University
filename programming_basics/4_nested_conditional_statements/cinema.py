projection = input()
rows = int(input())
columns = int(input())

tickets = rows * columns

if projection == 'Premiere':
    tickets *= 12
elif projection == 'Normal':
    tickets *= 7.50
elif projection == 'Discount':
    tickets *= 5

print(f'{tickets:.2f} leva')
