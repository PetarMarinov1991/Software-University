import re
regex = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for _ in range(int(input())):
    message = input()
    data = re.findall(regex, message)

    if data:
        for match in data:
            ascii_codes = [ord(char) for char in match[1]]
            ascii_codes = ' '.join(str(code) for code in ascii_codes)
            print(f'{match[0]}: {ascii_codes}')
    else:
        print('The message is invalid')
