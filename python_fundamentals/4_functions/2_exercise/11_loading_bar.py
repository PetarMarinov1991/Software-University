def loading_bar(num):
    n = num // 10
    bar = ['%'] * n + ['.'] * (10 - n)
    if '.' in bar:
        return f'{num}% [{"".join(bar)}]\nStill loading...'
    return f'100% Complete!\n[{"".join(bar)}]'


number = int(input())
print(loading_bar(number))
