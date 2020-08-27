import re

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

for _ in range(int(input())):
    data = re.findall(pattern, input())
    if data:
        for match in data:
            boss_name, title = match[0], match[1]
            print(f'{boss_name}, The {title}')
            print(f'>> Strength: {len(boss_name)}')
            print(f'>> Armour: {len(title)}')
    else:
        print('Access denied!')
