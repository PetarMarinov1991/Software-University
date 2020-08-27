dictionary = dict()

for i in range(int(input())):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word, synonyms in dictionary.items():
    print(f'{word} – {", ".join([word for word in synonyms])}')
