file_path = './files/File Opener/text.txt'

try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')
