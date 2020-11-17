class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_idx = 0
        self.list_length = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx <= self.list_length:
            temp_idx = self.current_idx
            self.current_idx += 1
            return self.iterable[::-1][temp_idx]
        raise StopIteration()
