movie_name = input()
package = input()
tickets = int(input())

price = 0
discount = 0
is_discount = False

if movie_name == 'John Wick':
    if package == 'Drink':
        price = 12
    elif package == 'Popcorn':
        price = 15
    elif package == 'Menu':
        price = 19

elif movie_name == 'Star Wars':
    if package == 'Drink':
        price = 18
    elif package == 'Popcorn':
        price = 25
    elif package == 'Menu':
        price = 30

    if tickets >= 4:
        is_discount = True
        discount = 0.70

elif movie_name == 'Jumanji':
    if package == 'Drink':
        price = 9
    elif package == 'Popcorn':
        price = 11
    elif package == 'Menu':
        price = 14

    if tickets == 2:
        is_discount = True
        discount = 0.85

if is_discount:
    bill = (price * tickets) * discount
else:
    bill = price * tickets

print(f'Your bill is {bill:.2f} leva.')
