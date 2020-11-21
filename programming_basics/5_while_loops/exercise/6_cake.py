w = int(input())
h = int(input())
cake_size = w * h

pieces = 0

while pieces <= cake_size:
    pieces_taken = input()

    if not pieces_taken == 'STOP':
        pieces += int(pieces_taken)
    if pieces_taken == 'STOP':
        break

cake_left = cake_size - pieces

if pieces > cake_size:
    print(f'No more cake left! You need {abs(cake_left)} pieces more.')
else:
    print(f'{cake_left} pieces are left.')
