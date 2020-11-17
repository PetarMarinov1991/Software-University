def get_primes(integers):
    for num in integers:
        is_prime = True
        if num > 1:
            for divisor in range(2, num):
                if num % divisor == 0:
                    is_prime = False
            if is_prime:
                yield num
