fuel_type = input()
fuel_amount = float(input())
club_card = input()

liter_gasoline = 2.22
liter_diesel = 2.33
liter_gas = 0.93

fuel_price = 0

if fuel_type == 'Gasoline':
    if club_card == 'Yes':
        fuel_price = fuel_amount * (liter_gasoline - 0.18)
    else:
        fuel_price = fuel_amount * liter_gasoline
elif fuel_type == 'Diesel':
    if club_card == 'Yes':
        fuel_price = fuel_amount * (liter_diesel - 0.12)
    else:
        fuel_price = fuel_amount * liter_diesel
elif fuel_type == 'Gas':
    if club_card == 'Yes':
        fuel_price = fuel_amount * (liter_gas - 0.08)
    else:
        fuel_price = fuel_amount * liter_gas

if fuel_amount > 25:
    fuel_price = fuel_price * 0.90
elif fuel_amount >= 20:
    fuel_price = fuel_price * 0.92

print(f'{fuel_price:.2f} lv.')
