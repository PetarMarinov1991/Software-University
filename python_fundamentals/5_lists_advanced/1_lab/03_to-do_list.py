to_do_list = {}

command = input()

while command != 'End':
    args = command.split('-')
    idx, do = int(args[0]), args[1]

    to_do_list[idx] = do

    command = input()

sorted_dict = {k: v for k, v in sorted(to_do_list.items(), key=lambda x: x[0])}
to_do = [v for k, v in sorted_dict.items()]

print(to_do)
