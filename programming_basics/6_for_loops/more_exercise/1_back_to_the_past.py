inheritance = float(input())
going_to_year = int(input())

current_year = 1800
age = 18
money_needed = 12000

for year in range(current_year, going_to_year + 1):
    if year % 2 == 0:
        inheritance -= money_needed
    else:
        inheritance -= money_needed + 50 * age

    age += 1

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')
