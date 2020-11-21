suitcase_width = int(input())
suitcase_height = int(input())
suitcase_debt = int(input())
priority_ticket = input()

suitcase_volume = suitcase_debt * suitcase_height * suitcase_width
luggage_tax = 0

if suitcase_volume > 200:
    if priority_ticket == "true":
        luggage_tax = 20
    else:
        luggage_tax = 100
elif suitcase_volume > 100:
    if priority_ticket == "true":
        luggage_tax = 10
    else:
        luggage_tax = 50
elif suitcase_volume > 50:
    if priority_ticket == "true":
        luggage_tax = 0
    else:
        luggage_tax = 25

print(f'Luggage tax: {luggage_tax:.2f}')



