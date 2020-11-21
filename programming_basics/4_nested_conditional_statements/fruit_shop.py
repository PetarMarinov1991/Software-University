fruit = input()
day = input()
quantity = float(input())

fruit_price = 0
is_fruit = True
day_of_week = True

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        fruit_price += 2.50
    elif fruit == 'apple':
        fruit_price += 1.20
    elif fruit == 'orange':
        fruit_price += 0.85
    elif fruit == 'grapefruit':
        fruit_price += 1.45
    elif fruit == 'kiwi':
        fruit_price += 2.70
    elif fruit == 'pineapple':
        fruit_price += 5.50
    elif fruit == 'grapes':
        fruit_price += 3.85
    else:
        is_fruit = False
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        fruit_price += 2.70
    elif fruit == 'apple':
        fruit_price += 1.25
    elif fruit == 'orange':
        fruit_price += 0.90
    elif fruit == 'grapefruit':
        fruit_price += 1.60
    elif fruit == 'kiwi':
        fruit_price += 3.00
    elif fruit == 'pineapple':
        fruit_price += 5.60
    elif fruit == 'grapes':
        fruit_price += 4.20
    else:
        is_fruit = False
else:
    day_of_week = False

bill = fruit_price * quantity
if day_of_week and is_fruit:
    print(f'{bill:.2f}')
else:
    print('error')

