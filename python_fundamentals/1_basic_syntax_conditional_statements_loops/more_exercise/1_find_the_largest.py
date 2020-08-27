num = input()

arr_digits = []


def find_max_num(digits):
    digits.sort(reverse=True)
    number = ''.join(digits)

    return number


for digit in range(len(num)):
    arr_digits.append(num[digit])

print(find_max_num(arr_digits))
