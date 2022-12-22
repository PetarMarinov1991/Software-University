employees_happiness = [int(x) for x in input().split()]
factor = int(input())

happiness_factor = [e * factor for e in employees_happiness]
average = sum(happiness_factor) / len(employees_happiness)
happy = [e for e in happiness_factor if e >= average]
sad = [e for e in happiness_factor if e not in happy]

happiness = 'Employees are not happy!' if len(happy) <= len(sad) else 'Employees are happy!'
print(f'Score: {len(happy)}/{len(employees_happiness)}. {happiness}')
