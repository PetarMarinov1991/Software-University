string = input()


def capital_indices(s):
    return [i for i in range(len(string)) if string[i].isupper()]


print(capital_indices(string))
