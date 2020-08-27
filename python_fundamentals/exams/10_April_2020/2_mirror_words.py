import re
regex = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

mirror_words = []

data = re.findall(regex, input())

for match in data:
    if match[1] == match[2][::-1]:
        mirror_words.append(match[1] + ' <=> ' + match[2])

if len(data) == 0:
    print('No word pairs found!')
else:
    print(f'{len(data)} word pairs found!')

if mirror_words:
    print('The mirror words are:')
    print(', '.join([match for match in mirror_words]))
else:
    print('No mirror words!')
