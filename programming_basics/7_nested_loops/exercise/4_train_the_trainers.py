judges = int(input())

presentation = input()
total_grade_sum = 0
counter = 0

while presentation != 'Finish':
    presentation_grade_sum = 0

    for _ in range(judges):
        grade = float(input())
        presentation_grade_sum += grade
        total_grade_sum += grade

    average_presentation_grade = presentation_grade_sum / judges
    print(f'{presentation} - {average_presentation_grade:.2f}.')

    counter += 1

    presentation = input()

final_average_grade = total_grade_sum / (judges * counter)
print(f'Student\'s final assessment is {final_average_grade:.2f}.')
