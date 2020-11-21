food_money = float(input())
souvenir_money = float(input())
hotel_money = float(input())

DISTANCE = 210
liters_fuel = (DISTANCE * 2) / 100 * 7
fuel_money = liters_fuel * 1.85
three_days_stay = 3 * food_money + 3 * souvenir_money
first_day_in_hotel = hotel_money * 0.9
second_day_in_hotel = hotel_money * 0.85
third_day_in_hotel = hotel_money * 0.8
total_stay_in_hotel = first_day_in_hotel + second_day_in_hotel + third_day_in_hotel

total_sum = fuel_money + three_days_stay + total_stay_in_hotel
print(f'Money needed: {total_sum:.2f}')
