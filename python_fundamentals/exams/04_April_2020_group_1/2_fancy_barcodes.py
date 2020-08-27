import re
regex = r"@#{1,}([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})@#{1,}"

for _ in range(int(input())):
    barcode = re.search(regex, input())

    product_group = ''

    if barcode:
        barcode = barcode.group(1)
        for char in barcode:
            if char.isdigit():
                product_group += char
        if product_group == '':
            print('Product group: 00')
        else:
            print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
