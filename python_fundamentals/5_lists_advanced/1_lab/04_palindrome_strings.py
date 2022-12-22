from itertools import count


def is_palindrome(word):
    return word == word[::-1]


words = [s for s in input().split()]
palindrome_searched = input()

palindromes = [word for word in words if is_palindrome(word)]
palindrome_searched_count = palindromes.count(palindrome_searched)

print(f'{palindromes}\nFound palindrome {palindrome_searched_count} times')
