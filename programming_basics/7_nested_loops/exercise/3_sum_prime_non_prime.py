primes = list()
non_primes = list()

command = input()

while command != 'stop':
    number = int(command)

    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    divisor = number
    divisors = list()

    while divisor > 0:
        if number % divisor == 0:
            divisors.append(divisor)
            if len(divisors) > 2:
                non_primes.append(number)
                break
            if len(divisors) == 2 and divisor == 1:
                primes.append(number)
        divisor -= 1

    command = input()

print(f'Sum of all prime numbers is: {sum(primes)}')
print(f'Sum of all non prime numbers is: {sum(non_primes)}')
