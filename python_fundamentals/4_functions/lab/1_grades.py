def solve(grade):
    grades = {
        2.00 <= grade <= 2.99: 'Fail',
        3.00 <= grade <= 3.49: 'Poor',
        3.50 <= grade <= 4.49: 'Good',
        4.50 <= grade <= 5.49: 'Very Good',
        5.50 <= grade <= 6.00: 'Excellent'
    }
    return grades.get(1)


print(solve(grade=float(input())))
