def encrypt_vigenere_chiffre():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        key = input("Key: ").lower().strip()
        if all(char in alphabet for char in key):
            break
        else:
            print("Invalid input")
    while True:
        text = input("Text: ").lower().strip()
        if all(char in alphabet for char in text):
            break
        else:
            print("Invalid input")
    encrypted_text = ""
    for n, text_char in enumerate(text):
        current_shift = alphabet.index(key[n % len(key)])
        encrypted_text += alphabet[(alphabet.index(text_char) + current_shift) % 26]
    print(f"Encrypted text: {encrypted_text}")


def decrypt_vigenere_chiffre():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        key = input("Key: ").lower().strip()
        if all(char in alphabet for char in key):
            break
        else:
            print("Invalid input")
    while True:
        text = input("Encrypted text: ").lower().strip()
        if all(char in alphabet for char in text):
            break
        else:
            print("Invalid input")
    text = ""
    for n, text_char in enumerate(text):
        current_shift = alphabet.index(key[n % len(key)])
        text += alphabet[(alphabet.index(text_char) - current_shift) % 26]
    print(f"Text: {text}")


def encrypt_or_decrypt():
    while True:
        choice = input("Process: ").lower().strip()
        if choice == "encrypt":
            encrypt_vigenere_chiffre()
            break
        elif choice == "decrypt":
            decrypt_vigenere_chiffre()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    encrypt_or_decrypt()
