def best_list_pureness(*args):
    my_list, k = args[0], args[1]
    rotations = 0
    best_pureness = 0
    for i in range(k + 1):
        current_pureness = 0
        for idx, num in enumerate(my_list):
            current_pureness += num * idx
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotations = i
        last = my_list.pop()
        my_list.insert(0, last)
    return f'Best pureness {best_pureness} after {rotations} rotations'
