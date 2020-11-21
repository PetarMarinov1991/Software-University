cargo_count = int(input())

trains = 0
trucks = 0
vans = 0

for cargo in range(cargo_count):
    tons = int(input())

    if tons >= 12:
        trains += tons
    elif tons > 3:
        trucks += tons
    else:
        vans += tons

total_cargo = vans + trucks + trains
average_cargo = (vans * 200 + trucks * 175 + trains * 120) / total_cargo

van_percentage = vans / total_cargo * 100
truck_percentage = trucks / total_cargo * 100
train_percentage = trains / total_cargo * 100

print(f'{average_cargo:.2f}')
print(f'{van_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
