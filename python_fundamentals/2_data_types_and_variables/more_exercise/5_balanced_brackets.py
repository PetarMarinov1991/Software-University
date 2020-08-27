lines = int(input())

is_opened = False
is_balanced = True

for i in range(lines):
    string = input()
    string = string.strip()

    if string == '(':
        if not is_opened:
            is_opened = True
        else:
            is_balanced = False

    if string == ')':
        if is_opened:
            is_opened = False
        else:
            is_balanced = False

if is_balanced and not is_opened:
    print('BALANCED')
else:
    print('UNBALANCED')
