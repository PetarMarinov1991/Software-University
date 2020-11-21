from math import floor as fl

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
astronaut_height = float(input())

ship_volume = ship_width * ship_length * ship_height
room_volume = (astronaut_height + 0.40) * 4
space_for = fl(ship_volume / room_volume)

if space_for < 3:
    print("The spacecraft is too small.")
elif space_for <= 10:
    print(f"The spacecraft holds {space_for} astronauts.")
else:
    print("The spacecraft is too big.")
