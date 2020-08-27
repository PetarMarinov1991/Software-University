days = int(input())
budget = float(input())
people = int(input())
fuel_km = float(input())
food_one_person = float(input())
room_one_person = float(input())

total_expenses = 0
hotel_expenses = days * people * room_one_person
food_expenses = days * people * food_one_person

if people > 10:
    total_expenses = food_expenses + 0.75 * hotel_expenses
else:
    total_expenses = food_expenses + hotel_expenses

for day in range(1, days + 1):
    distance = float(input())
    total_expenses += distance * fuel_km
    if day % 3 == 0 or day % 5 == 0:
        total_expenses *= 1.4
    if day % 7 == 0:
        total_expenses -= total_expenses / people
    diff = budget - total_expenses
    if diff < 0:
        print(f'Not enough money to continue the trip. You need {abs(diff):.2f}$ more.')
        break

if budget >= total_expenses:
    print(f'You have reached the destination. You have {budget - total_expenses:.2f}$ budget left.')
