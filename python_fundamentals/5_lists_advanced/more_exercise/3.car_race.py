racing_track = [int(x) for x in input().split()]

first_racer = racing_track[0:len(racing_track) // 2]
second_racer = racing_track[len(first_racer) + 1:][::-1]

sum_first_racer = 0
sum_second_racer = 0

for n in first_racer:
    if n == 0:
        sum_first_racer *= 0.8
    else:
        sum_first_racer += n

for n in second_racer:
    if n == 0:
        sum_second_racer *= 0.8
    else:
        sum_second_racer += n

winner = 'right'
total_time = sum_second_racer

if sum_first_racer < sum_second_racer:
    winner = 'left'
    total_time = sum_first_racer

print(f'The winner is {winner} with total time: {total_time:.1f}')
