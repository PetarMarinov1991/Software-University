def aliquot_sum(num):
    divisors_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor

    return divisors_sum


def perfect_number(num):
    if aliquot_sum(num) == n:
        return 'We have a perfect number!'

    return "It's not so perfect."


n = int(input())
print(perfect_number(n))
