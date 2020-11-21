command = input()

ascii_sum = 0
most_ascii_sum = 0
most_powerful_word = ''
vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y')

while command != 'End of words':
    word = command
    ascii_sum = 0
    for index in range(len(word)):
        letter = ord(word[index])
        ascii_sum += letter

    if word[0] in vowels:
        ascii_sum *= len(word)
    else:
        ascii_sum = round(ascii_sum / len(word))

    if ascii_sum > most_ascii_sum:
        most_ascii_sum = ascii_sum
        most_powerful_word = word

    command = input()
    if command == 'End of words':
        print(f'The most powerful word is {most_powerful_word} - {most_ascii_sum}')
