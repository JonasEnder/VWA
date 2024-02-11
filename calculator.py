alphabet = list("abcdefghijklmnopqrstuvwxyz")


def calculate_value(string: str):
    output = 0
    original_string = string
    for i in range(3):
        index = alphabet.index(string[i])
        output += index * (26 ** (2 - i))
    print(f"{original_string} >>> {output}")


def calculate_shift(number: int):
    output = ""
    original_number = number
    for i in range(3):
        power = 26 ** (2 - i)
        digit = number // power
        output += alphabet[digit]
        number = number % power
    print(f"{original_number} >>> {output}")
