def replace_char(text):
    for char in text:
        if char in ['-', ',', '.', '!', '?']:
            text = text.replace(char, '@')
    return text


def reverse_words(text):
    return ' '.join(text.split()[::-1])


def output(file_path):
    result = ''
    try:
        with open(file_path) as file:
            line = file.readline()
            index = 0
            while line:
                if index % 2 == 0:
                    line = replace_char(line)
                    result += reverse_words(line) + '\n'
                index += 1
                line = file.readline()
    except FileNotFoundError:
        return 'File not found'
    return result


print(output('./files/Even Lines/text.txt'))
