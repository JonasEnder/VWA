alphabet = list("abcdefghijklmnopqrstuvwxyz")

wheel_outputs = [list("ekmflgdqvzntowyhxuspaibrcj"), list("ajdksiruxblhwtmcqgznpyfvoe"),
                 list("bdfhjlcprtxvznyeiwgakmusqo"), list("esovpzjayquirhxlnftgkdcmwb"),
                 list("vzbrgityupsdnhlxawmjqofeck")]

wheel_notches = ["q", "e", "v", "j", "z"]


class EnigmaBaseObject:

    def __init__(self, name=""):
        self.name = name
        self.arrows = ["\t"] * 26
        self.shifted_alphabet = alphabet.copy()
        self.forward_mapping = {letter: letter for letter in alphabet}
        self.backward_mapping = {letter: letter for letter in alphabet}

    def map_forwards(self, input_index):
        shifted_alphabet_copy = list(map(str.lower, self.shifted_alphabet.copy()))
        input_letter = shifted_alphabet_copy[input_index]
        output_letter = self.forward_mapping[input_letter]
        output_index = shifted_alphabet_copy.index(output_letter)
        self.arrows[input_index] = ">>>"
        return output_index

    def map_backwards(self, input_index):
        shifted_alphabet_copy = list(map(str.lower, self.shifted_alphabet.copy()))
        input_letter = shifted_alphabet_copy[input_index]
        output_letter = self.backward_mapping[input_letter]
        output_index = shifted_alphabet_copy.index(output_letter)
        self.arrows[output_index] = "<<<"
        return output_index

    def clear_arrows(self):
        self.arrows = ["\t"] * 26


class Plugboard(EnigmaBaseObject):

    def __init__(self, name="P", plugboard_pairs=None):
        super().__init__(name)
        if plugboard_pairs:
            for pair in plugboard_pairs:
                self.forward_mapping[pair[0]] = pair[1]
                self.forward_mapping[pair[1]] = pair[0]
                self.backward_mapping[pair[0]] = pair[1]
                self.backward_mapping[pair[1]] = pair[0]


class Wheel(EnigmaBaseObject):

    def __init__(self, number, ring_position, wheel_position):
        super().__init__(str(number + 1))
        self.output_side = wheel_outputs[number]
        self.ring_position = ring_position
        self.wheel_position = wheel_position
        self.notch_position = wheel_notches[number]
        self.shift_alphabet(self.wheel_position)
        self.apply_ring_position()
        self.build_mapping()
        self.replace_notch(self.notch_position)

    def shift_alphabet(self, shift):
        self.shifted_alphabet = [self.shifted_alphabet[(n + shift) % 26] for n in range(26)]

    def increase_wheel_position(self):
        self.wheel_position += 1
        self.wheel_position %= 26
        self.shift_alphabet(1)

    def apply_ring_position(self):
        self.output_side = [self.output_side[(n - self.ring_position) % 26] for n in range(26)]
        self.output_side = [alphabet[(alphabet.index(self.output_side[n]) + self.ring_position) % 26] for
                            n in range(26)]

    def build_mapping(self):
        for n in range(26):
            self.forward_mapping[alphabet[n]] = self.output_side[n]
            self.backward_mapping[self.output_side[n]] = alphabet[n]

    def replace_notch(self, notch_positon):
        self.shifted_alphabet[self.shifted_alphabet.index(notch_positon)] = notch_positon.upper()

class Reflector(EnigmaBaseObject):

    def __init__(self, name="R"):
        super().__init__(name)
        temp = list("yruhqsldpxngokmiebfzcwvjat")
        for n in range(26):
            self.forward_mapping[alphabet[n]] = temp[n]

    def map_forwards(self, input_index):
        input_letter = self.shifted_alphabet[input_index]
        output_letter = self.forward_mapping[input_letter]
        output_index = self.shifted_alphabet.index(output_letter)
        self.arrows[self.shifted_alphabet.index(input_letter)] = ">>>"
        self.arrows[self.shifted_alphabet.index(output_letter)] = "<<<"
        return output_index


class Enigma:

    def __init__(self, wheel_order, ring_positions, wheel_positions, plugboard_pairs=None):
        self.enigma_base_objects = []
        self.wheels = []
        self.wheel_positions = []
        self.previous_wheel_positions = []
        self.text = ""
        self.coded_text = ""
        self.turn = 0
        self.input_letter = ""
        self.output_letter = ""
        self.plugboard = Plugboard(plugboard_pairs=plugboard_pairs)
        self.enigma_base_objects.append(self.plugboard)
        self.entry_wheel = EnigmaBaseObject(name="E")
        self.enigma_base_objects.append(self.entry_wheel)
        for i in range(3):
            wheel = Wheel(number=wheel_order[i], ring_position=ring_positions[i], wheel_position=wheel_positions[i])
            self.enigma_base_objects.append(wheel)
            self.wheels.append(wheel)
        self.reflector = Reflector()
        self.enigma_base_objects.append(self.reflector)

    def update_wheel_positions(self):
        self.previous_wheel_positions = self.wheel_positions
        self.wheel_positions = []
        for wheel in self.wheels:
            self.wheel_positions.append(wheel.wheel_position)
        self.wheel_positions.reverse()

    def clear_arrows(self):
        for enigma_base_objects in self.enigma_base_objects:
            enigma_base_objects.clear_arrows()

    def turn_wheels(self):
        self.turn += 1
        foo = self.wheels[0].shifted_alphabet[0]
        bar = self.wheels[1].shifted_alphabet[0]
        self.wheels[0].increase_wheel_position()
        if foo == self.wheels[0].notch_position.upper():
            self.wheels[1].increase_wheel_position()
        if bar == self.wheels[1].notch_position.upper():
            self.wheels[1].increase_wheel_position()
            self.wheels[2].increase_wheel_position()

    def show_table(self):
        output = "\n\t"
        for enigma_base_object in self.enigma_base_objects:
            output += f"{enigma_base_object.name}\t"
        print(output)
        print("-"*25)
        for i in range(26):
            output = f"{alphabet[i].upper()}"
            for enigma_base_object in self.enigma_base_objects:
                output += enigma_base_object.arrows[i]
                output += enigma_base_object.shifted_alphabet[i]
            print(output)

    def scramble_letter(self, input_letter):
        index = alphabet.index(input_letter)
        for enigma_base_object in self.enigma_base_objects:
            index = enigma_base_object.map_forwards(index)
        for enigma_base_object in self.enigma_base_objects[4::-1]:  # without reflector
            index = enigma_base_object.map_backwards(index)
        return alphabet[index]

    def code_letter(self, input_letter):
        self.turn_wheels()
        self.clear_arrows()
        self.update_wheel_positions()
        output_letter = self.scramble_letter(input_letter)
        return output_letter

    def run(self):
        self.update_wheel_positions()
        while True:
            print(f"\n{'{}-{}-{}'.format(*[number + 1 for number in self.wheel_positions])}/{'{}-{}-{}'.format(*[alphabet[number].upper() for number in self.wheel_positions])}")
            print(f"Text: {self.text.upper()}")
            print(f"Coded text: {self.coded_text.upper()}")
            stripped_input = input("Input: ").lower().replace(" ", "")
            try:
                if stripped_input == ".exit":
                    break
                elif stripped_input == ".help":
                    ...
                elif stripped_input == ".show":
                    self.show_table()
                else:
                    for letter in stripped_input:
                        _ = alphabet.index(letter)
                    for letter in stripped_input:
                        self.coded_text += self.code_letter(letter)
                    self.text += stripped_input
            except ValueError:
                print("Invalid input")
