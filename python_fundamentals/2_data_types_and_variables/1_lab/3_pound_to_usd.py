def convert_pound_to_usd(pound):
    return f'{pound * 1.31:.3f}'


pound = int(input())

print(convert_pound_to_usd(pound))
