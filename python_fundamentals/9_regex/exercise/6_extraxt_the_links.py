import re
regex = r"(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

while True:
    text = input()

    if not text:
        break

    links = [x[0] for x in re.findall(regex, text)]

    for link in links:
        print(''.join(links))
