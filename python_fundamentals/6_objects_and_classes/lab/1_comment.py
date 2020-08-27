class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


name = input()
comment = Comment(f'{name}', 'qj mi huq')

print(f'{comment.username} {comment.content}')
print(f'{comment.likes}')
