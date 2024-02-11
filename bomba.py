from enigma import Enigma

from input_functions import *

alphabet = list("abcdefghijklmnopqrstuvwxyz")


class Bomba:

    def __init__(self):
        self.wheel_positions = []
        self.pseudo_enigmas = []
        self.reference_letters = []
        self.pseudo_enigmas_outputs = []
        self.wheel_order = input_wheel_order()
        self.wheel_order.reverse()
        for n in range(6):
            ring_position = [0, 0, 0]
            ring_position.reverse()
            wheel_position = input_wheel_positions()
            wheel_position.reverse()
            self.wheel_positions.append(wheel_position)
            reference_letter = input_reference_letter()
            self.reference_letters.append(reference_letter)
            pseudo_enigma = Enigma(self.wheel_order, ring_position, wheel_position)
            self.pseudo_enigmas.append(pseudo_enigma)

            for wheel in pseudo_enigma.wheels:
                wheel.notch_position = "z"
                wheel.replace_notch(wheel.notch_position)

    def print_pseudo_enigmas_outputs(self):
        for count, output in enumerate(self.pseudo_enigmas_outputs):
            reference_letter = self.reference_letters[count].upper()
            output = output.upper()
            wheel_positions_numbers = [n+1 for n in self.pseudo_enigmas[count].previous_wheel_positions]
            wheel_positions_letters = [alphabet[n].upper() for n in self.pseudo_enigmas[count].previous_wheel_positions]
            print(
                f"{reference_letter} >>> {output} at {'{}-{}-{}'.format(*wheel_positions_numbers)}/{'{}-{}-{}'.format(*wheel_positions_letters)}")

    def break_code(self):
        for i in range(17575):
            for count, pseudo_enigma in enumerate(self.pseudo_enigmas):
                pseudo_enigma_output = pseudo_enigma.code_letter(self.reference_letters[count])
                self.pseudo_enigmas_outputs.append(pseudo_enigma_output)
            if self.found_possible_answer():
                print(f"\nPossible solution:")
                self.print_pseudo_enigmas_outputs()
            self.pseudo_enigmas_outputs = []
        print("\nEnd of machine period")

    def found_possible_answer(self):
        if all(self.pseudo_enigmas_outputs[n] == self.pseudo_enigmas_outputs[n + 1] for n in range(0, 6, 2)):
            return True
        else:
            return False


if __name__ == "__main__":
    bomba = Bomba()
    bomba.break_code()
