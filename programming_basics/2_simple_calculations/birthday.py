length = int(input())
width = int(input())
height = int(input())
filled_volume = 1 - float(input()) * 0.01

total_volume = length * width * height * 0.001
needed_liters = total_volume * filled_volume

print(f'{needed_liters:.3f}')


