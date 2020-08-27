odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    current_sum = 0
    name = input()
    for ch in name:
        current_sum += ord(ch)
    current_sum //= i
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

if sum(odd_set) > sum(even_set):
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))
elif sum(even_set) > sum(odd_set):
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))
else:
    print(', '.join([str(x) for x in odd_set.intersection(even_set)]))
