import matplotlib.pyplot


def plot_letter_frequency():
    count = 0
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    amount = [0] * 26
    inp = input("Text: ").lower().strip()
    for char in inp:
        try:
            amount[alphabet.index(char)] += 1
            count += 1
        except ValueError:
            print("Invalid input")
    matplotlib.pyplot.bar(alphabet, amount, color="black", fill=False, hatch="/////")
    matplotlib.pyplot.xlabel("Letter")
    matplotlib.pyplot.ylabel("Amount")
    matplotlib.pyplot.show()


if __name__ == "__main__":
    plot_letter_frequency()
