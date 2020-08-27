starting_salary = float(input())
expenses = float(input())
increasing = float(input())
car_price = float(input())
months = int(input())

total_earnings = 0

for month in range(months):
    total_earnings += starting_salary + increasing * month
    total_earnings -= expenses

if total_earnings >= car_price:
    print('Have a nice ride!')
else:
    print('Work harder!')
