def calculate_racer_time(racer):
    racer_time = 0
    for time in racer:
        if time == 0:
            racer_time *= 0.8
        else:
            racer_time += time
    return racer_time


def determine_winner(time_1, time_2):
    side = 'left' if time_1 < time_2 else 'right'
    return f'The winner is {side} with total time: {min(time_1, time_2):.1f}'


numbers = [int(x) for x in input().split()]
half_distance = len(numbers) // 2

first_racer = numbers[:half_distance]
second_racer = numbers[half_distance + 1:][::-1]

first_racer_time = calculate_racer_time(first_racer)
second_racer_time = calculate_racer_time(second_racer)

print(determine_winner(first_racer_time, second_racer_time))
