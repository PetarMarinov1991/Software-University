def grade_in_words(grade):
    grades = {
        'Fail': [2.00, 2.99],
        'Poor': [3.00, 3.49],
        'Good': [3.50, 4.49],
        'Very Good': [4.50, 5.49],
        'Excellent': [5.50, 6.00]
    }

    for key, value in grades.items():
        if key[0] <= grade <= key[1]:
            return key


grade = float(input())
print(grade_in_words(grade))
