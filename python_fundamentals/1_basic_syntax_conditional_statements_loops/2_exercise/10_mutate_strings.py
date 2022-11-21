first_string = input()
second_string = input()

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:

        new_string = ''

        for j in range(0, i + 1):
            new_string += second_string[j]
        for k in range(i + 1, len(first_string)):
            new_string += first_string[k]

        print(new_string)
