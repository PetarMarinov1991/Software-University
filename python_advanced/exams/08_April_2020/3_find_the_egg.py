def find_strongest_eggs(*arg):
    seq, num = arg[0], arg[1]
    sub_lists = [seq[i::num] for i in range(num)]
    strong_eggs = []
    for sub_list in sub_lists:
        mid = len(sub_list) // 2
        first_half, second_half = sub_list[:mid], sub_list[mid + 1:]

        if sub_list[mid - 1] < sub_list[mid] > sub_list[mid + 1]:
            if [True for i, j in zip(first_half, second_half) if i < j]:
                strong_eggs.append(sub_list[mid])
    return strong_eggs


# print(find_strongest_eggs([-1, 7, 3, 15, 2, 12], 2))
# print(find_strongest_eggs([-1, 0, 2, 5, 2, 3], 2))
# print(find_strongest_eggs([51, 21, 83, 52, 55], 1))
