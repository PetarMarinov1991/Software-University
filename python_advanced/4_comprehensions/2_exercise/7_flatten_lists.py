print(' '.join([str(i) for j in [x.split(' ') for x in input().split('|')[::-1]] for i in j if i.isdigit() or '-' in i]))
