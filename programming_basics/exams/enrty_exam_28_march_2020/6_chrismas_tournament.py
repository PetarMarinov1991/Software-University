days = int(input())

money = 0
day_won = 0
day_lost = 0

for day in range(days):
    daily_money = 0
    win = 0
    lose = 0

    while True:
        sport = input()

        if sport == 'Finish':
            break

        result = input()

        if result == 'win':
            win += 1
            daily_money += 20
        else:
            lose += 1

    if win > lose:
        daily_money *= 1.1
        day_won += 1
    else:
        day_lost += 1

    money += daily_money

if day_won > day_lost:
    print(f'You won the tournament! Total raised money: {money * 1.2:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money:.2f}')
