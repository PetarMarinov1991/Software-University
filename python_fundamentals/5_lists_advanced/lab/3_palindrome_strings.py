words = input().split()
searched = input()

palindromes = [word for word in words if word == word[::-1]]

print(palindromes)
print(f'Found palindrome {palindromes.count(searched)} times')
