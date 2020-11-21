movie_name = input()
cinema_type = input()
tickets_sold = int(input())

ticket_price = 0

if cinema_type == 'normal':
    if movie_name == 'A Star Is Born':
        ticket_price = 7.50
    elif movie_name == 'Bohemian Rhapsody':
        ticket_price = 7.35
    elif movie_name == 'Green Book':
        ticket_price = 8.15
    elif movie_name == 'The Favourite':
        ticket_price = 8.75

elif cinema_type == 'luxury':
    if movie_name == 'A Star Is Born':
        ticket_price = 10.50
    elif movie_name == 'Bohemian Rhapsody':
        ticket_price = 9.45
    elif movie_name == 'Green Book':
        ticket_price = 10.25
    elif movie_name == 'The Favourite':
        ticket_price = 11.55

elif cinema_type == 'ultra luxury':
    if movie_name == 'A Star Is Born':
        ticket_price = 13.50
    elif movie_name == 'Bohemian Rhapsody':
        ticket_price = 12.75
    elif movie_name == 'Green Book':
        ticket_price = 13.25
    elif movie_name == 'The Favourite':
        ticket_price = 13.95

income = tickets_sold * ticket_price
print(f'{movie_name} -> {income:.2f} lv.')
