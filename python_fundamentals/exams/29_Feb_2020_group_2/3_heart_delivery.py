neighborhood = list(map(int, input().split('@')))

jump = 0
success = 0

while True:
    line = input().split()
    command = line[0]

    if command == 'Love!':
        break

    if command == 'Jump':
        jump += int(line[1])
        if jump > len(neighborhood) - 1:
            jump = 0
        if neighborhood[jump] == 0:
            print(f'Place {jump} already had Valentine\'s day.')
            continue
        neighborhood[jump] -= 2
        if neighborhood[jump] == 0:
            print(f'Place {jump} has Valentine\'s day.')
            success += 1

fail = len(neighborhood) - success

print(f'Cupid\'s last position was {jump}.')
print(f'Cupid has failed {fail} places.')
