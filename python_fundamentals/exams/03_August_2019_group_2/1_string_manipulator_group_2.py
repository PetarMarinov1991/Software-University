string = input()

while True:
    line = input().split()

    if line[0] == 'Done':
        break

    if line[0] == 'Change':
        string = string.replace(line[1], line[2])
        print(string)
    elif line[0] == 'Includes':
        print(line[1] in string)
    elif line[0] == 'End':
        print(string.endswith(line[1]))
    elif line[0] == 'Uppercase':
        string = string.upper()
        print(string)
    elif line[0] == 'FindIndex':
        print(string.index(line[1]))
    elif line[0] == 'Cut':
        string = string[int(line[1]):int(line[1]) + int(line[2])]
        print(string)
