elements = input().split()
bakery = dict()

for i in range(0, len(elements), 2):
    k, v = elements[i], elements[i + 1]
    bakery[k] = int(v)

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')
