def odd_or_even_sum(command, numbers):
    even_sum = sum([num for num in numbers if num % 2 == 0])
    odd_sum = sum(numbers) - even_sum
    if command == 'Odd':
        return odd_sum * len(numbers)
    return even_sum * len(numbers)


print(odd_or_even_sum(input(), [int(x) for x in input().split()]))
