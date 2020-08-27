print('<h1>\n' + '    ' + input() + '\n</h1>')
print('<article>\n' + '    ' + input() + '\n</article>')

while True:
    comment = input()

    if comment == 'end of comments':
        break

    print('<div>\n' + '    ' + comment + '\n</div>')
