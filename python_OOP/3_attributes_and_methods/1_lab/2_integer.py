from math import floor as fl


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(fl(value))
        return 'value is not a float'

    @classmethod
    def from_roman(cls, value):
        def decode_roman_numeral(roman):
            trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            values = [trans[r] for r in roman]
            return sum(val if val >= next_val else -val for val, next_val in zip(values[:-1], values[1:])) + values[-1]
        return cls(decode_roman_numeral(value))

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            if value.isdigit():
                return cls(int(value))
        return 'wrong type'

    def add(self, integer):
        if isinstance(integer.value, int):
            self.value += integer.value
            return self.value
        return 'number should be an Integer instance'
