class Glass:
    capacity = 250

    def space_left(self):
        return Glass.capacity - self.content

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        if ml <= Glass.space_left(self):
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f'{Glass.space_left(self)} ml left'
