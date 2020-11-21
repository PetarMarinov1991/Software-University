passengers = int(input())
bus_stops = int(input())

for stop in range(1, bus_stops + 1):
    passengers -= int(input())
    passengers += int(input())
    if stop % 2 == 0:
        passengers -= 2
    else:
        passengers += 2

print(f'The final number of passengers is : {passengers}')
