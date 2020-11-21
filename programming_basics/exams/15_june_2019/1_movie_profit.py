movie_title = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())

daily_tickets_price = tickets_count * ticket_price
total_tickets_price = daily_tickets_price * days_count
for_cinema = total_tickets_price * percentage_for_cinema / 100

income = total_tickets_price - for_cinema

print(f'The profit from the movie {movie_title} is {income:.2f} lv.')
