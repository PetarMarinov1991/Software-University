def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


def find_idx(word, my_list):
    return my_list.index(word)


def swap_word(idx_1, idx_2, my_list):
    my_list[idx_1], my_list[idx_2] = my_list[idx_2], my_list[idx_1]


sentence = input().split()

while True:
    line = input().split()
    command = line[0]

    if command == 'Stop':
        break

    if command == 'Delete':
        idx = int(line[1])
        if valid_idx(idx + 1, sentence):
            sentence.remove(sentence[idx + 1])
    elif command == 'Swap':
        word_1, word_2 = line[1], line[2]
        if word_1 in sentence and word_2 in sentence:
            idx_word_1, idx_word_2 = find_idx(word_1, sentence), find_idx(word_2, sentence)
            swap_word(idx_word_1, idx_word_2, sentence)
    elif command == 'Put':
        word, idx = line[1], int(line[2])
        if valid_idx(idx, sentence):
            sentence.insert(idx - 1, word)
    elif command == 'Sort':
        sentence.sort(reverse=True)
    elif command == 'Replace':
        word_1, word_2 = line[1], line[2]
        if word_2 in sentence:
            idx_word_2 = find_idx(word_2, sentence)
            sentence[idx_word_2] = word_1

print(' '.join([word for word in sentence]))
