number_of_lines = int(input())

max_snowball_value = 0
output = ''

for i in range(number_of_lines):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        output = f'{snowball_snow} : {snowball_time} = {max_snowball_value} ({snowball_quality})'

print(output)
