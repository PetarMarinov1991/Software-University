n = int(input())
keyword = input()

original_list = [input() for _ in range(n)]
filtered_list = list(filter(lambda k: keyword in k, original_list))

print(original_list)
print(filtered_list)
