voucher_value = int(input())

is_valid = False
tickets_bought = 0
others_bought = 0

command = input()

while command != 'End':
    if len(command) > 8:
        ticket_price = ord(command[0]) + ord(command[1])
        if ticket_price <= voucher_value:
            is_valid = True
            tickets_bought += 1
            voucher_value -= ticket_price
        else:
            is_valid = False
    else:
        others_price = ord(command[0])
        if others_price <= voucher_value:
            is_valid = True
            others_bought += 1
            voucher_value -= others_price
        else:
            is_valid = False

    if not is_valid:
        print(tickets_bought)
        print(others_bought)
        break

    command = input()

    if command == 'End':
        print(tickets_bought)
        print(others_bought)
        break
