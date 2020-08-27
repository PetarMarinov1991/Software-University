num = int(input())

divisor = 1
divisors_count = 0

is_prime = True

while num >= divisor:
    if num % divisor == 0:
        divisors_count += 1
        if divisors_count > 2:
            is_prime = False
            break

    divisor += 1

print(is_prime)
