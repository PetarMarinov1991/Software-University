def reverse_text(string):
    for i in range(len(string)):
        yield string[::-1][i]
