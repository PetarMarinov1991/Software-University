def check_if_number_is_prime(num):
    prime = False
    if num > 1:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    return prime


num = int(input())
print(check_if_number_is_prime(num))
