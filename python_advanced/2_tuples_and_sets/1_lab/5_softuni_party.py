reservations = []
guests_arrived = []

for _ in range(int(input())):
    guest_number = input()

    if len(guest_number) == 8:
        reservations.append(guest_number)

while True:
    arrived = input()

    if arrived == 'END':
        break

    if len(arrived) == 8:
        guests_arrived.append(arrived)

difference = set(reservations) - set(guests_arrived)
print(len(difference))
for guest in sorted(difference):
    print(guest)
