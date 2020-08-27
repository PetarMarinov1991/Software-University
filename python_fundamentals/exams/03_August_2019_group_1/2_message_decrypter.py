import re

regex = r"([\$|%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for _ in range(int(input())):
    line = input()

    if line.startswith('%') or line.startswith('$'):
        data = re.findall(regex, line)

        if data:
            for match in data:
                message = match[1]
                numbers = [match[2], match[3], match[4]]
                print(f'{message}: {"".join([chr(int(x)) for x in numbers])}')
        else:
            print('Valid message not found!')
    else:
        print('Valid message not found!')
