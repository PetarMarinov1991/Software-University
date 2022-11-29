def convert_centuries_to_minutes(centuries):
    years = centuries * 100
    days = int(years * 365.2422)
    hours = days * 24
    minutes = hours * 60
    return f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes'


centuries = int(input())

print(convert_centuries_to_minutes(centuries))
