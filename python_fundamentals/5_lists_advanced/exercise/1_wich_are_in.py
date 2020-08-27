searched_words = input().split(', ')
words = input().split(', ')

result = []

for search_word in searched_words:
    for word in words:
        if search_word in word and search_word not in result:
            result.append(search_word)

print(result)
