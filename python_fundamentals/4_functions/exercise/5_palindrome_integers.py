def is_palindrome(num_str):
    length = len(num_str)
    palindrome = True

    for index in range(length // 2):
        if num_str[index] != num_str[length - 1 - index]:
            palindrome = False
            break

    return palindrome


numbers = input().split(', ')

for num in numbers:
    print(is_palindrome(num))
