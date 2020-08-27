biscuits_per_worker = int(input())
workers = int(input())
competing_company = int(input())

production = workers * biscuits_per_worker
produced = production * 20 + int(production * 0.75) * 10
diff = competing_company - produced
percentage = abs(diff) / competing_company * 100

more_or_less = 'more'

if diff > 0:
    more_or_less = 'less'

print(f'You have produced {produced} biscuits for the past month.')
print(f'You produce {percentage:.2f} percent {more_or_less} biscuits.')
