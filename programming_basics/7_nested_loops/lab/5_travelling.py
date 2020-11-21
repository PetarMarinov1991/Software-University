command = input()

while command != 'End':
    destination = command
    money_needed = float(input())

    while money_needed > 0:
        money_needed -= float(input())

    print(f'Going to {destination}!')

    command = input()
