def remove_volews(text):
    volews = ['a', 'o', 'u', 'e', 'i']
    return ''.join([x for x in text if x.lower() not in volews])


str_input = input()
print(remove_volews(str_input))
