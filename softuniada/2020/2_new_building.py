pattern = ['#', '.', '.', '.'] * 151

pattern_len = int(input())
rows = int(pattern_len + pattern_len / 2)
multiplier = 1

for i in range(rows):
    col = ''.join(pattern[i:pattern_len * multiplier])
    multiplier += 1
    print(col[:pattern_len])
