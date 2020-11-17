class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'y', 'u']
        self.idx = 0
        self.string_length = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= self.string_length:
            temp = self.idx
            self.idx += 1
            if self.string[temp].lower() in self.vowels:
                return self.string[temp]
            return self.__next__()
        raise StopIteration()
