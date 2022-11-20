budget = int(input())

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    product_price = int(command)
    budget -= product_price

    if budget < 0:
        print('You went in overdraft!')
        break
