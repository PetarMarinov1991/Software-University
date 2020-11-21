max_poor_grades = int(input())

last_task = None
total_tasks = 0
poor_grades_count = 0
total = 0
need_a_break = False

while poor_grades_count < max_poor_grades:
    current_task = input()
    if current_task == 'Enough':
        break
    grade = int(input())
    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == max_poor_grades:
            need_a_break = True
    total += grade
    total_tasks += 1
    last_task = current_task

average_grade = total / total_tasks

if need_a_break:
    print(f'You need a break, {poor_grades_count} poor grades.')
else:
    print(f'Average score: {average_grade:.2f}\nNumber of problems: {total_tasks}\nLast problem: {last_task}')
