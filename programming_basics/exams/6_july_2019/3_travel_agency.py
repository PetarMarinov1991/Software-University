town = input()
package = input()
is_VIP = input()
days = int(input())

price_per_day = 0

if days > 7:
    days -= 1

if town == 'Bansko' or town == 'Borovets':
    if package == 'noEquipment':
        price_per_day = 80
        if is_VIP == 'yes':
            price_per_day *= 0.95
    elif package == 'withEquipment':
        price_per_day = 100
        if is_VIP == 'yes':
            price_per_day *= 0.90

elif town == 'Varna' or town == 'Burgas':
    if package == 'noBreakfast':
        price_per_day = 100
        if is_VIP == 'yes':
            price_per_day *= 0.93
    elif package == 'withBreakfast':
        price_per_day = 130
        if is_VIP == 'yes':
            price_per_day *= 0.88

final_price = days * price_per_day

valid_town = town == 'Bansko' or town == 'Borovets' or town == 'Varna' or town == 'Burgas'
valid_package = package == 'noEquipment' or package == 'withEquipment' or package == 'noBreakfast' or package == 'withBreakfast'
invalid = False

if town == 'Bansko' or town == 'Borovets':
    if package != 'noEquipment' and package != 'withEquipment':
        invalid = True
elif town == 'Varna' or town == 'Burgas':
    if package != 'noBreakfast' and package != 'withBreakfast':
        invalid = True
elif not valid_town or valid_package:
    invalid = True

if invalid:
    print('Invalid input!')
elif days < 1:
    print('Days must be positive number!')
else:
    print(f'The price is {final_price:.2f}lv! Have a nice time!')
