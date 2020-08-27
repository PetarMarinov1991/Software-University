words = [word.lower() for word in input().split()]
words_dict = dict()

for word in words:
    if word not in words_dict:
        words_dict.update({word: 1})
    else:
        words_dict[word] += 1

print(' '.join([word for word, value in words_dict.items() if value % 2 != 0]))
