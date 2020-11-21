fuel_type = input()
liters_fuel = float(input())

if fuel_type != 'Diesel' and fuel_type != 'Gas' and fuel_type != 'Gasoline':
    print('Invalid fuel!')
elif liters_fuel >= 25:
    print(f'You have enough {fuel_type.lower()}.')
else:
    print(f'Fill your tank with {fuel_type.lower()}!')
