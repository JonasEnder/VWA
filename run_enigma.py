from enigma import Enigma

from input_functions import *

alphabet = list("abcdefghijklmnopqrstuvwxyz")


class Main:

    def __init__(self):
        self.wheel_order = input_wheel_order()
        self.wheel_order.reverse()
        self.ring_positions = input_ring_positions()
        self.ring_positions.reverse()
        self.wheel_positions = input_wheel_positions()
        self.wheel_positions.reverse()
        self.plugboard_pairs = input_plugboard_pairs()
        self.enigma = Enigma(self.wheel_order, self.ring_positions, self.wheel_positions, self.plugboard_pairs)

    def main_routine(self):
        self.enigma.run()


if __name__ == "__main__":
    main = Main()
    main.main_routine()

