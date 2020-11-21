budget = float(input())

command = input()

while command != 'ACTION':
    actor_name = command

    if len(actor_name) > 15:
        salary = budget * 0.20
    else:
        salary = float(input())

    budget -= salary

    if budget <= 0:
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break

    command = input()

    if command == 'ACTION':
        print(f'We are left with {budget:.2f} leva.')
