companies = dict()

while True:
    line = input().split(' -> ')

    if line[0] == 'End':
        break

    company, employee = line

    if company not in companies:
        companies.update({company: [employee]})
    else:
        if employee not in companies[company]:
            companies[company].append(employee)

for company, employees in sorted(companies.items()):
    print(f'{company}')
    for employee in employees:
        print(f'-- {employee}')
