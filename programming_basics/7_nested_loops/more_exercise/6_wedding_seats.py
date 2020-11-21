end = input()
sector = int(input())
seats = int(input())

seats_count = 0

for letter in range(ord('A'), ord(end) + 1):
    sector += 1
    for row in range(1, sector):
        if row % 2 == 1:
            odd_seats = [print(f'{chr(letter)}{row}{chr(seat)}') for seat in range(ord('a'), ord('a') + seats)]
            seats_count += len(odd_seats)
        else:
            even_seats = [print(f'{chr(letter)}{row}{chr(seat)}') for seat in range(ord('a'), ord('a') + seats + 2)]
            seats_count += len(even_seats)

print(seats_count)
