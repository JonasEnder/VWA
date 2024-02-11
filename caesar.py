def encrypt_caesar_chiffre():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        shift = input("Shift: ").strip()
        try:
            shift = int(shift)
            break
        except ValueError:
            print("Invalid input")
    while True:
        text = input("Text: ").lower().strip()
        if all(char in alphabet for char in text):
            break
        else:
            print("Invalid input")
    encrypted_text = "".join([alphabet[(alphabet.index(char) + shift) % 26] for char in text])
    print(f"Encrypted text: {encrypted_text}")


def decrypt_caesar_chiffre():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        shift = input("Shift: ").strip()
        try:
            shift = int(shift)
            break
        except ValueError:
            print("Invalid input")
    while True:
        encrypted_text = input("Encrypted text: ").lower().strip()
        if all(char in alphabet for char in encrypted_text):
            break
        else:
            print("Invalid input")
    text = "".join([alphabet[(alphabet.index(char) - shift) % 26] for char in encrypted_text])
    print(f"Text: {text}")

def encrypt_or_decrypt():
    while True:
        choice = input("Process: ").lower().strip()
        if choice == "encrypt":
            encrypt_caesar_chiffre()
            break
        elif choice == "decrypt":
            decrypt_caesar_chiffre()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    encrypt_or_decrypt()
