def decrypt_message(key, n):
    message = [chr(ord(input()) + key) for _ in range(n)]
    return ''.join(message)


key = int(input())
n = int(input())
print(decrypt_message(key, n))

