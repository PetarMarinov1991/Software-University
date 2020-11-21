number = float(input())
convert_from = input()
convert_to = input()

if convert_from == 'm':
    if convert_to == 'cm':
        number *= 100
    elif convert_to == 'mm':
        number *= 1000
elif convert_from == 'cm':
    if convert_to == 'm':
        number /= 100
    elif convert_to == 'mm':
        number *= 10
elif convert_from == 'mm':
    if convert_to == 'cm':
        number /= 10
    elif convert_to == 'm':
        number /= 1000

print(f'{number:.3f}')
