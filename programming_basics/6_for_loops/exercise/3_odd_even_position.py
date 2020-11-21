import sys

n = int(input())

even_sum = 0
odd_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_min = sys.maxsize
odd_max = -sys.maxsize

for i in range(n):
    num = float(input())
    if i % 2 != 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num

if n == 0:
    even_min = None
    even_max = None
    odd_min = None
    odd_max = None
if n == 1:
    even_min = None
    even_max = None

print(f'OddSum={odd_sum:.2f},')

if odd_min is not None:
    print(f'OddMin={odd_min:.2f},')
else:
    print('OddMin=No,')
if odd_max is not None:
    print(f'OddMax={odd_max:.2f},')
else:
    print('OddMax=No,')

print(f'EvenSum={even_sum:.2f},')

if even_min is not None:
    print(f'EvenMin={even_min:.2f},')
else:
    print('EvenMin=No,')
if even_max is not None:
    print(f'EvenMax={even_max:.2f}')
else:
    print('EvenMax=No')
