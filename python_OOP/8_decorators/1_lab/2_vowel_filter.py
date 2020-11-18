def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = {'a', 'o', 'e', 'i', 'u', 'y'}
        return [l for l in result if l in vowels]

    return wrapper
