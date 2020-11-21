country = input()
instrument = input()

score = 0

if country == 'Bulgaria':
    if instrument == 'ribbon':
        score = 19.000
    elif instrument == 'hoop':
        score = 19.300
    elif instrument == 'rope':
        score = 18.900
elif country == 'Russia':
    if instrument == 'ribbon':
        score = 18.500
    elif instrument == 'hoop':
        score = 19.100
    elif instrument == 'rope':
        score = 18.600
elif country == 'Italy':
    if instrument == 'ribbon':
        score = 18.700
    elif instrument == 'hoop':
        score = 18.800
    elif instrument == 'rope':
        score = 18.850

score_difference = 20 - score
percentage_to_max = (score_difference / 20) * 100

print(f'The team of {country} get {score:.3f} on {instrument}.')
print(f'{percentage_to_max:.2f}%')
