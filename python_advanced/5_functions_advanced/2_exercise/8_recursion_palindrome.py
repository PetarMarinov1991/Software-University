def palindrome(word, idx):
    word_as_list = [x for x in word]
    while word_as_list:
        if len(word_as_list) <= 1:
            return f'{word} is a palindrome'
        if word_as_list[idx] == word_as_list[-1]:
            word_as_list.pop(idx)
            word_as_list.pop(-1)
            palindrome(word_as_list, idx)
        else:
            return f'{word} is not a palindrome'
