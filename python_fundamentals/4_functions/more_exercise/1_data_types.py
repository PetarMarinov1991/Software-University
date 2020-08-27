def solve(data_type, data):
    result = ''
    if data_type == 'int':
        result = int(data) * 2
    elif data_type == 'real':
        result = f'{float(data) * 1.5:.2f}'
    elif data_type == 'string':
        result = f'${data}$'

    return result


print(solve(data_type=input(), data=input()))
