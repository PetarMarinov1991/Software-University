class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0
        self.large_sequence = self.sequence * 100

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.number:
            temp = self.idx
            self.idx += 1
            return self.large_sequence[temp]
        raise StopIteration()
