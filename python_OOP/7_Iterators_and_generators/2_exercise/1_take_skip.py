class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            self.counter += 1
            temp = self.current
            self.current += self.step
            return temp
        raise StopIteration()
