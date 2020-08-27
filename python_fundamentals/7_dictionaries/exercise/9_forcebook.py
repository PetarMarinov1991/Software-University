def user_exist():
    for key, value in force_book.items():
        if user in value:
            if not switch:
                return True
            return force_book[key].remove(user)


def choose_side():
    if side not in force_book:
        force_book[side] = []
    return force_book[side].append(user)


force_book = dict()

while True:
    line = input()

    if line == 'Lumpawaroo':
        break

    switch = True

    if '|' in line:
        switch = False
        line = line.split(' | ')
        side, user = line
        if not user_exist():
            choose_side()
    elif '->' in line:
        line = line.split(' -> ')
        user, side = line
        user_exist()
        choose_side()
        print(f'{user} joins the {side} side!')

force_book = {k: v for k, v in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0]))}

for side, users in force_book.items():
    if force_book[side]:
        print(f'Side: {side}, Members: {len(users)}')
        for user in sorted(users):
            print(f'! {user}')
