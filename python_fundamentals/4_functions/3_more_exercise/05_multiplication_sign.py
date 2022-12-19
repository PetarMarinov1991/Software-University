def define_sing(nums):
    if 0 in nums:
        return 'zero'
    if len([x for x in nums if x < 0]) % 2 != 0:
        return 'negative'
    return 'positive'


numbers = [int(input()) for _ in range(3)]

print(define_sing(numbers))
