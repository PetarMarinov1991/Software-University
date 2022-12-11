def number_filter(numbers, category):
    if category == 'even':
        return [x for x in numbers if x % 2 == 0]
    elif category == 'odd':
        return [x for x in numbers if x % 2 != 0]
    elif category == 'negative':
        return [x for x in numbers if x < 0]
    elif category == 'positive':
        return [x for x in numbers if x >= 0]


n = int(input())
numbers = [int(input()) for _ in range(n)]
category = input()

print(number_filter(numbers, category))
