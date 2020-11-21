all_nums = [int(input()) for _ in range(int(input()))]

p1 = [num for num in all_nums if num % 2 == 0]
p2 = [num for num in all_nums if num % 3 == 0]
p3 = [num for num in all_nums if num % 4 == 0]

print(f'{len(p1) / len(all_nums) * 100:.2f}%')
print(f'{len(p2) / len(all_nums) * 100:.2f}%')
print(f'{len(p3) / len(all_nums) * 100:.2f}%')
