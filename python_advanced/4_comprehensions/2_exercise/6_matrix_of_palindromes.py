rows, cols = [int(x) for x in input().split()]
print('\n'.join([' '.join([chr(97 + i) + chr(97 + i + j) + chr(97 + i) for j in range(cols)]) for i in range(rows)]))
