user_names = input().split(', ')
banned = ['!@#$%^&*()']

valid_users = ''

for user in user_names:
    if len(user) in range(3, 17):
        if user.isalnum() or user.__contains__('-') or user.__contains__('_'):
            for char in user:
                if char not in banned:
                    valid_users += char
            valid_users += ' '

valid_users = valid_users.split()
print('\n'.join(valid_users))
