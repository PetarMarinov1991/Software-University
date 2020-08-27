numbers = list(map(int, input().split()))
factor = int(input())

employees = [x * factor for x in numbers]
average_factor = sum(employees) / len(employees)
happy_employees = len([x for x in employees if x >= average_factor])

if happy_employees >= len(employees) / 2:
    print(f'Score: {happy_employees}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{len(employees)}. Employees are not happy!')
