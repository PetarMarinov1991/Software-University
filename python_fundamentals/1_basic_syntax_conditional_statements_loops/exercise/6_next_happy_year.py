year = int(input())
int_year = int(year)
current_year = []
happy_year = ''
happy_new_year = False

while happy_new_year is False:
    int_year += 1
    year = str(int_year)
    current_year = []

    for index in range(len(year)):
        current_year += year[index]
        happy_year = set(current_year)

        if int_year == int(''.join(current_year)):
            continue

    if len(happy_year) == len(year) and year != happy_year:
        happy_new_year = True

if happy_new_year:
    print(year)
