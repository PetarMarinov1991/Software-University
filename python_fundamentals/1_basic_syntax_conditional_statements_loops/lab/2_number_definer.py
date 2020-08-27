num = float(input())
value = ''

if num > 0:
    value = 'positive'
    if 0 < num < 1:
        value = 'small ' + value
    if num > 1000000:
        value = 'large ' + value
elif num < 0:
    value = 'negative'
    if -1 < num < 0:
        value = 'small ' + value
    elif num < -1000000:
        value = 'large ' + value
else:
    value = 'zero'

print(value)
