from math import floor as fl

record_in_sec = float(input())
distance_in_m = float(input())
time_per_m = float(input())

time_in_sec = distance_in_m * time_per_m + fl(distance_in_m / 50) * 30

if time_in_sec < record_in_sec:
    print(f'Yes! The new record is {time_in_sec:.2f} seconds.')
else:
    print(f'No! He was {time_in_sec - record_in_sec:.2f} seconds slower.')
