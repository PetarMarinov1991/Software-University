import string
import os

file_path = './files/Even Lines/text.txt'
output = 'output.txt'

if os.path.exists(file_path):
    with open(file_path) as file_path:
        line = file_path.readline()
        index = 1
        while line:
            letters_count = sum(line.count(x) for x in string.ascii_letters)
            punctuation_count = sum(line.count(x) for x in string.punctuation)
            with open(output, 'a') as file:
                file.write(f'Line {index}: {line} ({letters_count})({punctuation_count})\n')
            index += 1
            line = file_path.readline()
