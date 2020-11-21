nylon_sqr_m = int(input())
paint_l = int(input())
diluent_l = int(input())
work_hours = int(input())

nylon_price = (nylon_sqr_m + 2) * 1.50
paint_price = paint_l * 1.10 * 14.50
diluent_price = diluent_l * 5

cost = nylon_price + paint_price + diluent_price + 0.40
workers_salary = cost * 0.30 * work_hours
total = cost + workers_salary

print(f'Total expenses: {total:.2f} lv.')
