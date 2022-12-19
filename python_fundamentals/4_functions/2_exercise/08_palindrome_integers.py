def reversed_num(nums):
    return [int(x) for x in [str(x)[::-1] for x in nums]]


def is_palindrome(nums):
    return [nums[i] == reversed_num(nums)[i] for i in range(len(nums))]


numbers = [int(x) for x in input().split(', ')]

for x in is_palindrome(numbers):
    print(x)
