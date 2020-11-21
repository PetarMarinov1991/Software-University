contract_length = input()
contract_type = input()
internet = input()
num_of_fees = int(input())

contract_price = 0
internet_price = 0
discount = False

if contract_length == 'one':

    if contract_type == 'Small':
        contract_price = 9.98
    elif contract_type == 'Middle':
        contract_price = 18.99
    elif contract_type == 'Large':
        contract_price = 25.98
    elif contract_type == 'ExtraLarge':
        contract_price = 35.99

elif contract_length == 'two':
    discount = True

    if contract_type == 'Small':
        contract_price = 8.58
    elif contract_type == 'Middle':
        contract_price = 17.09
    elif contract_type == 'Large':
        contract_price = 23.59
    elif contract_type == 'ExtraLarge':
        contract_price = 31.79

if internet == 'yes':

    if contract_price > 30:
        internet_price = 3.85
    elif contract_price <= 10:
        internet_price = 5.50
    else:
        internet_price = 4.35

total = (contract_price + internet_price) * num_of_fees

if discount:
    total *= 0.9625

print(f'{total:.2f} lv.')
