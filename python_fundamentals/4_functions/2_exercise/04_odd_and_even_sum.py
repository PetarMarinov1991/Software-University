def odd_and_even_sum(num):
    filtered_digits = [int(x) for x in str(num) if x.isdigit()]

    def odd_sum():
        odd_digits = [x for x in filtered_digits if x % 2 != 0]
        return sum(odd_digits)

    def even_sum():
        even_digits = [x for x in filtered_digits if x % 2 == 0]
        return sum(even_digits)

    return f'Odd sum = {odd_sum()}, Even sum = {even_sum()}'


number = int(input())
print(odd_and_even_sum(number))
