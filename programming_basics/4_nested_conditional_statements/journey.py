budget = float(input())
season = input()

money_spend = 0
destination = None
accommodation = None

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        money_spend = budget * 0.3
    elif season == 'winter':
        accommodation = 'Hotel'
        money_spend = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        money_spend = budget * 0.4
    elif season == 'winter':
        accommodation = 'Hotel'
        money_spend = budget * 0.8
else:
    destination = 'Europe'
    accommodation = 'Hotel'
    money_spend = budget * 0.9

if budget >= money_spend:
    print(f'Somewhere in {destination}\n {accommodation} - {money_spend:.2f}')

