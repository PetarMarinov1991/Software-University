class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dict_length = len(dictionary) - 1
        self.dict_keys = list(dictionary.keys())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= self.dict_length:
            temp = self.idx
            self.idx += 1
            return self.dict_keys[temp], self.dictionary[self.dict_keys[temp]]
        raise StopIteration()
