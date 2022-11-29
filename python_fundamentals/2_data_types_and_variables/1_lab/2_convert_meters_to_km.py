def convert_m_to_km(m):
    return f'{m / 1000:.2f}'


meters = int(input())

print(convert_m_to_km(meters))
