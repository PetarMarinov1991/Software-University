string = input().lower()
substrings = ['sand', 'water', 'fish', 'sun']
substrings_count = sum([string.count(s) for s in substrings])

print(substrings_count)
