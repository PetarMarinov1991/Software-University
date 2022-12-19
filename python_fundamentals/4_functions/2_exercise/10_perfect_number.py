def aliquot_sum(n):
    numbers = [i for i in range(1, n) if n % i == 0]
    if sum(numbers) == n:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


num = int(input())
print(aliquot_sum(num))
