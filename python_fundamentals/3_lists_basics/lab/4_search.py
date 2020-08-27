lines = int(input())
word = input()

full_list = []
filtered_list = []

for i in range(lines):
    string = input()
    full_list.append(string)

    if word in string:
        filtered_list.append(string)

print(full_list)
print(filtered_list)
