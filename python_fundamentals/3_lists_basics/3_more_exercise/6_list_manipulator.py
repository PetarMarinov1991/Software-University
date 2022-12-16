def valid_index(i, arr):
    return i in range(len(arr))


def even_nums(arr):
    return [x for x in arr if x % 2 == 0]


def odd_nums(arr):
    return [x for x in arr if x % 2 != 0]


def max_idx(arr, max_value):
    return max([i for i, value in enumerate(arr) if value == max_value])


def get_first_x_numbers(count, even_or_odd, arr, first_or_last):
    original_arr = arr
    arr = even_nums(arr) if even_or_odd == 'even' else odd_nums(arr)
    if not arr:
        return []
    if count > len(arr):
        return arr if arr and count in range(len(original_arr)+1) else 'Invalid count'
    return [arr[i] for i in range(count)] if first_or_last == 'first' else \
        [(arr[::-1])[i] for i in range(count)][::-1]


nums = [int(x) for x in input().split()]

command = input()

while command != 'end':
    args = command.split()

    if args[0] == 'exchange':
        idx = int(args[1])
        if valid_index(idx, nums):
            nums = nums[idx + 1:] + nums[:idx + 1]
        else:
            print('Invalid index')
    elif args[0] == 'max':
        if args[1] == 'even' and even_nums(nums):
            max_even = max(even_nums(nums))
            print(max_idx(nums, max_even))
        elif args[1] == 'odd' and odd_nums(nums):
            max_odd = max(odd_nums(nums))
            print(max_idx(nums, max_odd))
        else:
            print('No matches')
    elif args[0] == 'min':
        if args[1] == 'even' and even_nums(nums):
            min_even = min(even_nums(nums))
            print(max_idx(nums, min_even))
        elif args[1] == 'odd' and odd_nums(nums):
            min_odd = min((odd_nums(nums)))
            print(max_idx(nums, min_odd))
        else:
            print('No matches')
    elif args[0] == 'first' or 'last':
        count, even_or_odd = int(args[1]), args[2]
        print(get_first_x_numbers(count, even_or_odd, nums, args[0]))

    command = input()

print(nums)
