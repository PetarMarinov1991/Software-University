def loading_bar(num):
    bar = []
    for _ in range(1, num, 10):
        bar.append('%')
    for _ in range(len(bar), 10):
        bar.append('.')

    output = '[' + ''.join(bar) + ']'

    if '.' in bar:
        return f'{n}% {output}\n' \
               'Still loading...'
    return '100% Complete!' \
           f'\n{output}'


n = int(input())
print(loading_bar(n))
