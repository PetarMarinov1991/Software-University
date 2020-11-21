money_needed = float(input())
money_owned = float(input())

spend_counter = 0
day_counter = 0
save = True

while money_owned < money_needed:
    command = input()
    money = float(input())

    day_counter += 1

    if command == 'save':
        money_owned += money
        spend_counter = 0
    elif command == 'spend':
        money_owned -= money
        spend_counter += 1
        if money_owned < 0:
            money_owned = 0

        if spend_counter == 5:
            save = False
            break
if save:
    print(f'You saved the money for {day_counter} days.')
else:
    print(f'You can\'t save the money.\n{day_counter}')
