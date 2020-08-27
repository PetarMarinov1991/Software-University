def valid_user(user, collection):
    if user not in collection:
        collection[user] = [0, 0]
    return collection


def sort_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: (-x[1][0], x[0]))}
    return my_dict


followers = dict()

while True:
    line = input().split(': ')
    command = line[0]

    if command == 'Log out':
        break

    username = line[1]
    if command == 'New follower':
        valid_user(username, followers)
    elif command == 'Like':
        valid_user(username, followers)
        followers[username][0] += int(line[2])
    elif command == 'Comment':
        valid_user(username, followers)
        followers[username][1] += 1
    elif command == 'Blocked':
        if username not in followers:
            print(f'{username} doesn\'t exist.')
        else:
            del followers[username]

print(f'{len(followers)} followers')
for username, likes in sort_dict(followers).items():
    print(f'{username}: {sum(likes)}')
