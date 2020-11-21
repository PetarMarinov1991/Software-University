budget = float(input())
ticket_category = input()
people = int(input())

transport_expenses = 0
ticket_price = 0

if people > 50:
    transport_expenses = budget * 0.25
elif people > 24:
    transport_expenses = budget * 0.4
elif people > 9:
    transport_expenses = budget * 0.5
elif people > 4:
    transport_expenses = budget * 0.6
elif people >= 1:
    transport_expenses = budget * 0.75

if ticket_category == 'VIP':
    ticket_price = 499.99
elif ticket_category == 'Normal':
    ticket_price = 249.99

total_expenses = (budget - transport_expenses) - (ticket_price * people)

if total_expenses >= 0:
    print(f'Yes! You have {total_expenses:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(total_expenses):.2f} leva.')
