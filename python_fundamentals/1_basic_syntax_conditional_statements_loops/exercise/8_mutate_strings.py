word1 = input()
word2 = input()

for index in range(len(word1)):
    if word1[index] != word2[index]:
        for index1 in range(0, index + 1):
            print(word2[index1], end='')

        for index2 in range(index + 1, len(word1)):
            print(word1[index2], end='')
        print()
