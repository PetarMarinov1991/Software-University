# # simple solution
# from math import factorial
#
# a = int(input())
# b = int(input())
#
# print(f'{factorial(a) / factorial(b):.2f}')


# # solution without importing factorial
def calc_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


a = int(input())
b = int(input())

print(f'{calc_factorial(a) / calc_factorial(b):.2f}')
