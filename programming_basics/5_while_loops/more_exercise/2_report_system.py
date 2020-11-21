expected_money = int(input())

card_money = 0
cash_money = 0
counter = 0
card_counter = 0
cash_counter = 0

while expected_money > 0:
    payment = input()
    counter += 1
    if payment != 'End':
        payment = int(payment)
        if counter % 2 != 0:
            if payment > 100:
                print(f'Error in transaction!')
            else:
                print(f'Product sold!')
                cash_counter += 1
                expected_money -= payment
                cash_money += payment
        elif counter % 2 == 0:
            if payment < 10:
                print(f'Error in transaction!')
            else:
                print(f'Product sold!')
                card_counter += 1
                expected_money -= payment
                card_money += payment
    elif payment == 'End':
        print(f'Failed to collect required money for charity.')
        break

if expected_money <= 0:
    average_card_money = card_money / card_counter
    average_cash_money = cash_money / cash_counter
    print(f'Average CS: {average_cash_money:.2f}')
    print(f'Average CC: {average_card_money:.2f}')
