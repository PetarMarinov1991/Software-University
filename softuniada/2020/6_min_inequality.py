import sys

sublist_len = int(input())
main_list_len = int(input())

main_list = [int(input()) for _ in range(main_list_len)]

main_list = sorted(main_list)
min_diff = sys.maxsize

for i in range(sublist_len - 1, main_list_len):
    current_diff = main_list[i] - main_list[i - (sublist_len - 1)]

    if current_diff < min_diff:
        min_diff = current_diff

print(min_diff)
