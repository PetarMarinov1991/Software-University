keys = list(map(int, input().split()))

while True:
    text = input()

    if text == 'find':
        break

    encrypted = ''
    counter = 0
    for i in range(len(text)):
        char = ord(text[i]) - keys[counter]
        encrypted += chr(char)
        counter += 1
        if counter == len(keys):
            counter = 0

    resource = encrypted.split('&')[1]
    coordinates = encrypted.split('<')[1][:-1]

    print(f'Found {resource} at {coordinates}')
