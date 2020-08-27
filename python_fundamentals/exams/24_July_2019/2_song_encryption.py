def valid_artist(artist_name):
    valid_name = True
    if artist_name[0].isupper():
        for ch in artist_name[1:]:
            if not ch.islower() and ch not in [' ', "'"]:
                valid_name = False
                break
    else:
        valid_name = False
    return valid_name


def valid_song(song_name):
    valid_name = True
    for ch in song_name:
        if ch.islower() and ch != ' ':
            valid_name = False
            break
    return valid_name


def encrypt_string(my_key, my_string):
    encrypted_string = ''
    for ch in my_string:
        if ch not in [' ', "'"]:
            char = ord(ch) + my_key
            if ch.isupper():
                if char > ord('Z'):
                    char -= ord('Z')
                    char += ord('A') - 1
            elif ch.islower():
                if char > ord('z'):
                    char -= ord('z')
                    char += ord('a') - 1
        else:
            char = ord(ch)
        encrypted_string += chr(char)
    return encrypted_string


while True:
    line = input().split(':')

    if line[0] == 'end':
        break

    artist, song = line[0], line[1]
    if valid_artist(artist) and valid_song(song):
        encrypted_artist, encrypted_song = encrypt_string(len(artist), artist), encrypt_string(len(artist), song)
        print(f'Successful encryption: {encrypted_artist}@{encrypted_song}')
    else:
        print('Invalid input!')
