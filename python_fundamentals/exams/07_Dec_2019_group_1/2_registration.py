import re
regex = r"U\$([A-Z]{1}[a-z]{2,})U\$P@\$([A-Za-z]{5,}[0-9]{1,})P@\$"

successful_registrations = 0

for _ in range(int(input())):
    data = re.findall(regex, input())

    if data:
        print('Registration was successful')
        successful_registrations += 1
        for match in data:
            print(f'Username: {match[0]}, Password: {match[1]}')
    else:
        print('Invalid username or password')

print(f'Successful registrations: {successful_registrations}')
