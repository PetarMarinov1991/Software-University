deg = float(input())
weather = None

if deg < 5 or deg > 35:
    weather = 'unknown'
elif deg < 12:
    weather = 'Cold'
elif deg < 15:
    weather = 'Cool'
elif deg < 20.1:
    weather = 'Mild'
elif deg < 26:
    weather = 'Warm'
elif deg <= 35.00:
    weather = 'Hot'

print(weather)
