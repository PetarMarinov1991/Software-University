import re

delimiters = ['<p>', '</p>']
escape = '|'.join(map(re.escape, delimiters))
regex = r'<html>\\n<head><title>(Some title)</title></head>\\n<body>(Here<p>is some</p>content)' \
        r'<a href="www.somesite.com">\\n(click)</body>\\n</html>'

text = re.split(escape, input())
text = ' '.join(text)
data = re.search(regex, text)

if data:
    title, content, link = data.group(1), data.group(2), data.group(3)
    print(f'Title: {title}')
    print(f'Content: {content} {link}')
