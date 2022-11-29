def find_happy_year(year):
    # all digits of the year must be different

    is_happy_year = False

    while not is_happy_year:
        year += 1
        digits = [int(x) for x in str(year)]
        if len(set(digits)) >= len(str(year)):
            is_happy_year = True

    return year


year = int(input())
print(find_happy_year(year))
