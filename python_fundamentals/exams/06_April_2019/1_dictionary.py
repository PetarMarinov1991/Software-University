dictionary = dict()
words_to_check = []

while True:
    data = input().split(' | ')

    if data[0] in ['End', 'List']:
        break

    for part in data:
        if ':' in part:
            part = part.split(': ')
            word, definition = part[0], part[1]

            if word not in dictionary:
                dictionary[word] = []
            dictionary[word].append(definition)
        else:
            words_to_check = data

for word, definitions in dictionary.items():
    definitions.sort(key=len, reverse=True)

dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda x: x)}

if data[0] == 'List':
    print(' '.join(dictionary.keys()))
else:
    for word in words_to_check:
        print(word)
        for definition in dictionary[word]:
            print(f'-{definition}')
