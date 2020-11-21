town = input()
sells = float(input())

commission = 0
is_town = True

if town == 'Sofia':
    if sells > 10000:
        commission = sells * 0.12
    elif sells > 1000:
        commission = sells * 0.08
    elif sells > 500:
        commission = sells * 0.07
    elif sells >= 0:
        commission = sells * 0.05
elif town == 'Varna':
    if sells > 10000:
        commission = sells * 0.13
    elif sells > 1000:
        commission = sells * 0.10
    elif sells > 500:
        commission = sells * 0.075
    elif sells >= 0:
        commission = sells * 0.045
elif town == 'Plovdiv':
    if sells > 10000:
        commission = sells * 0.145
    elif sells > 1000:
        commission = sells * 0.12
    elif sells > 500:
        commission = sells * 0.08
    elif sells >= 0:
        commission = sells * 0.055
else:
    is_town = False

if is_town and sells >= 0:
    print(f'{commission:.2f}')
else:
    print('error')
