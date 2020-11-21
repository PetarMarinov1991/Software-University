stage = input()
ticket = input()
tickets_count = int(input())
picture = input()

ticket_price = 0
total_price = 0

if stage == 'Quarter final':
    if ticket == 'Standard':
        ticket_price += 55.50
    elif ticket == 'Premium':
        ticket_price += 105.20
    elif ticket == 'VIP':
        ticket_price += 118.90

elif stage == 'Semi final':
    if ticket == 'Standard':
        ticket_price += 75.88
    elif ticket == 'Premium':
        ticket_price += 125.22
    elif ticket == 'VIP':
        ticket_price += 300.40

elif stage == 'Final':
    if ticket == 'Standard':
        ticket_price += 110.10
    elif ticket == 'Premium':
        ticket_price += 160.66
    elif ticket == 'VIP':
        ticket_price += 400.00

total_price = ticket_price * tickets_count

free_picture = False

if total_price > 4000:
    total_price *= 0.75
    free_picture = True

elif total_price > 2500:
    total_price *= 0.9

if picture == 'Y' and free_picture == False:
    total_price += 40 * tickets_count

print(f'{total_price:.2f}')
