import sys

flight = input()
least_minutes_stay = sys.maxsize

while flight != 'End':
    ticket_number = flight
    ticket_price = int(input())
    minutes_stay = int(input())
    flight = input()

    if minutes_stay < least_minutes_stay:
        least_minutes_stay = minutes_stay
        current_ticket_number = ticket_number
        current_ticket_price = ticket_price * 1.96

hours = int(least_minutes_stay / 60)
minutes = least_minutes_stay % 60

if flight == 'End':
    print(f'Ticket found for flight {current_ticket_number} costs {current_ticket_price:.2f} leva with {hours}h {minutes}m stay')

