journey_cost = float(input())
months = int(input())

money_collected = 0

for month in range(1, months + 1):
    if month % 2 == 1 and month > 1:
        money_collected *= 0.84
    elif month % 4 == 0:
        money_collected *= 1.25
    money_collected += journey_cost * 0.25

diff = abs(journey_cost - money_collected)

if journey_cost <= money_collected:
    print(f'Bravo! You can go to Disneyland and you will have {diff:.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {diff:.2f}lv. more.')
