import string

words_path = './files/Words Count/words.txt'
input_path = './files/Words Count/text.txt'

words_dict = dict()

try:
    with open(words_path, 'r') as file:
        words = file.readline().split()
        words_dict = {word: 0 for word in words}
    with open(input_path, 'r') as file:
        text = file.readlines()
        for word in words:
            for line in text:
                line.translate(str.maketrans('', '', string.punctuation))
                if word.lower() in line.lower():
                    words_dict[word] += 1
        for word, count in sorted(words_dict.items(), key=lambda x: -x[1]):
            print(f'{word} - {count}')
except FileNotFoundError:
    print('File not found')
