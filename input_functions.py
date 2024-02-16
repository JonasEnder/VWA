alphabet = list("abcdefghijklmnopqrstuvwxyz")


def input_wheel_order():
    while True:
        wheels = ["I", "II", "III", "IV", "V"]
        removable_wheels = wheels.copy()
        split_input = input("Wheel order: ").strip().split(" ")
        try:
            if not len(split_input) == 3:
                raise ValueError
            wheel_order = []
            for item in split_input:
                _ = removable_wheels.index(item)
                wheel_order.append(wheels.index(item))
                removable_wheels.remove(item)
            return wheel_order
        except ValueError:
            print("Invalid input")


def input_ring_positions():
    while True:
        split_input = input("Ring positions: ").strip().lower().split(" ")
        try:
            ring_positions = [alphabet.index(item) for item in split_input]
            if len(ring_positions) == 3:
                break
            else:
                raise ValueError
        except ValueError:
            try:
                ring_positions = [int(item) - 1 for item in split_input]
                if all(number in range(26) for number in ring_positions):
                    if len(ring_positions) == 3:
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input")
    return ring_positions


def input_wheel_positions():
    while True:
        split_input = input("Wheel positions: ").strip().lower().split(" ")
        try:
            wheel_positions = [alphabet.index(item) for item in split_input]
            if len(wheel_positions) == 3:
                break
            else:
                raise ValueError
        except ValueError:
            try:
                wheel_positions = [int(item) - 1 for item in split_input]
                if all(number in range(26) for number in wheel_positions):
                    if len(wheel_positions) == 3:
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input")
    return wheel_positions


def input_plugboard_pairs():
    while True:
        removable_alphabet = list("abcdefghijklmnopqrstuvwxyz")
        user_input = input("Plugboard pairs: ").strip().lower()
        if user_input:
            try:
                for item in user_input:
                    _ = removable_alphabet.index(item)
                    removable_alphabet.remove(item)
                    split_input = user_input.split(" ")
                    if all(len(item) == 2 for item in split_input):
                        plugboard_pairs = split_input
                        return plugboard_pairs
                    else:
                        raise ValueError
            except ValueError:
                print("Invalid input")
        else:
            return None


def input_reference_letter():
    while True:
        user_input = input("Reference letter: ").lower().strip()
        try:
            _ = alphabet.index(user_input)
            return user_input
        except ValueError:
            print("Invalid input")
