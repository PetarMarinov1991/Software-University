def sum_numbers(first_num, second_num):
    return a + b


def subtract(first_num, second_num):
    return a - b


def add_and_subtract(first_num, second_num, third_num):
    return sum_numbers(a, b) - c


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(first_num=a, second_num=b, third_num=c))
