from random import choice


class RandomList(list):
    def get_random_element(self):
        element_to_remove = choice(self)
        return element_to_remove
