junior_bikers = int(input())
senior_bikers = int(input())
route_type = input()

charge_junior = 0
charge_senior = 0

if route_type == 'trail':
    charge_junior = 5.5
    charge_senior = 7
elif route_type == 'cross-country':
    charge_junior = 8
    charge_senior = 9.5
    if junior_bikers + senior_bikers >= 50:
        charge_junior -= charge_junior * 0.25
        charge_senior -= charge_senior * 0.25
elif route_type == 'downhill':
    charge_junior = 12.25
    charge_senior = 13.75
elif route_type == 'road':
    charge_junior = 20
    charge_senior = 21.5

total_charge = junior_bikers * charge_junior + senior_bikers * charge_senior
expenses = total_charge * 0.05
money_left = total_charge - expenses

print(f'{money_left:.2f}')
