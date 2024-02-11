from enigma import Enigma

from input_functions import input_wheel_order, input_ring_positions

from secrets import choice

alphabet = list("abcdefghijklmnopqrstuvwxyz")


class KeyGenerator:

    def __init__(self):
        self.wheel_order = input_wheel_order()
        self.wheel_order.reverse()
        print(self.wheel_order)
        self.ring_positions = input_ring_positions()
        self.ring_positions.reverse()
        print(self.ring_positions)

    def generate_keys(self):
        for i in range(5000):
            wheel_order = self.wheel_order
            ring_positions = self.ring_positions
            wheel_positions = [choice(range(26)), choice(range(26)), choice(range(26))]
            wheel_positions.reverse()
            enigma = Enigma(wheel_order, ring_positions, wheel_positions)
            wheel_positions.reverse()
            random_key = [choice(alphabet), choice(alphabet), choice(alphabet)]
            encoded_key = []
            for j in range(2):
                for letter in random_key:
                    encoded_letter = enigma.code_letter(letter)
                    encoded_key.append(encoded_letter)
            for j in range(3):
                if encoded_key[j] == "e" and encoded_key[j + 3] == "e":
                    print([alphabet[n] for n in wheel_positions], random_key, encoded_key)


if __name__ == "__main__":
    key_generator = KeyGenerator()
    key_generator.generate_keys()
