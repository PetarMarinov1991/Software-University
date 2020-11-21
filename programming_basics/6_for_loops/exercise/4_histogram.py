all_nums = [int(input()) for _ in range(int(input()))]

p1 = [num for num in all_nums if num < 200]
p2 = [num for num in all_nums if 200 <= num <= 399]
p3 = [num for num in all_nums if 400 <= num <= 599]
p4 = [num for num in all_nums if 600 <= num <= 799]
p5 = [num for num in all_nums if num >= 800]

print(f'{len(p1) / len(all_nums) * 100:.2f}%')
print(f'{len(p2) / len(all_nums) * 100:.2f}%')
print(f'{len(p3) / len(all_nums) * 100:.2f}%')
print(f'{len(p4) / len(all_nums) * 100:.2f}%')
print(f'{len(p5) / len(all_nums) * 100:.2f}%')
