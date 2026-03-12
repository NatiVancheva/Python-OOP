from math import floor
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(floor(float_value))
    
    @classmethod
    def from_roman(cls, value):
        roman_to_int = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(value):
            current = roman_to_int[char]

            if current < prev_value:
                total -= current
            else:
                total += current
            
            prev_value = current
            
        return cls(total)