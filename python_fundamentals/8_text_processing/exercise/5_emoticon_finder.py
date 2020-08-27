text = input()
emoticons = ''

for idx, char in enumerate(text):
    if ':' == char:
        emoticons += text[idx]
        emoticons += text[idx + 1]
        emoticons += ' '

print('\n'.join(emoticons.split()))
