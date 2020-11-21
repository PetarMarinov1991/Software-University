import sys

n = int(input())

current_sum = 0
diff = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())

    max_sum = num1 + num2

    if i > 0:
        diff = abs(current_sum - max_sum)

    current_sum = max_sum

if diff > 0:
    print(f'No, maxdiff={diff}')
else:
    print(f'Yes, value={current_sum}')
