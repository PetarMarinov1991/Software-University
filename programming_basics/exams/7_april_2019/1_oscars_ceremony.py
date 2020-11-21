rent_of_hall = int(input())

statuettes_price = rent_of_hall * 0.7
catering_price = statuettes_price * 0.85
music_price = catering_price / 2

total_costs = statuettes_price + catering_price + music_price + rent_of_hall

print(f'{total_costs:.2f}')
