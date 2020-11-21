import math
record_sec = float(input())
distance_m = float(input())
m_per_second = float(input())

water_resistance = math.floor(distance_m / 15)
slow_down = water_resistance * 12.5
swim_time = distance_m * m_per_second
total_swim_time = swim_time + slow_down

if record_sec > total_swim_time:
    print(f'Yes, he succeeded! The new world record is {total_swim_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_swim_time - record_sec:.2f} seconds slower.')
