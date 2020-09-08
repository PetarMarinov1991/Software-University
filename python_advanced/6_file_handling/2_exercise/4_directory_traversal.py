import os

path = input()
files_dict = dict()

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split('.')[1]
        if extension not in files_dict:
            files_dict[extension] = []
        files_dict[extension].append(file)

result = ''
for key, value in sorted(files_dict.items()):
    result += f'.{key}' + '\n'
    for file in sorted(value):
        result += f'- - - {file}' + '\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
location = desktop + os.path.sep + 'report.txt'

with open(location, 'w') as file:
    file.write(result)
