nums = [int(x) for x in input().split()]
average_num = sum(nums) / len(nums)
top_nums = sorted([num for num in nums if num > average_num])[::-1]

if top_nums:
    print(' '.join(str(num) for num in top_nums[:5]))
else:
    print('No')
