import re

regex = r"([*|@])([A-Z][a-z]{2,})\1: \[([A-Za-z])]\|\[([A-Za-z])]\|\[([A-Za-z])]\|"

for _ in range(int(input())):
    line = input()

    if len(line.split(': ')[1]) == 12:
        data = re.findall(regex, line)
        if data:
            for match in data:
                print(f'{match[1]}: {ord(match[2])} {ord(match[3])} {ord(match[4])}')
        else:
            print('Valid message not found!')
    else:
        print('Valid message not found!')
