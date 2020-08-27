import re

regex = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<(\1)"

for _ in range(int(input())):
    data = re.findall(regex, input())

    if data:
        for match in data:
            print(f'Password: {match[1]}{match[2]}{match[3]}{match[4]}')
    else:
        print('Try another password!')
