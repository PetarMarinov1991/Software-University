def add_elements(count):
    collection = set()
    for _ in range(count):
        collection.add(int(input()))
    return collection


first_range, second_range = [int(x) for x in input().split()]
first_set = add_elements(first_range)
second_set = add_elements(second_range)
print('\n'.join([str(num) for num in first_set.intersection(second_set)]))
