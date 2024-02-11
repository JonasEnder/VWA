import secrets


def encrypt_one_time_pad():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        text = input("Text: ").lower().strip()
        if all(char in alphabet for char in text):
            break
        else:
            print("Invalid input")
    key = [alphabet[secrets.choice(range(26))] for _ in text]
    print(f"Key: {''.join(key)}")
    encrypted_text = "".join(
        [alphabet[(alphabet.index(char) + alphabet.index(key[n])) % 26] for n, char in enumerate(text)])
    print(f"Encrypted text: {encrypted_text}")


def decrypt_one_time_pad():
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
    text = "".join([alphabet[(alphabet.index(char) - alphabet.index(key[n])) % 26] for n, char in enumerate(text)])
    print(f"Text: {text}")


def encrypt_or_decrypt():
    while True:
        choice = input("Process: ").lower().strip()
        if choice == "encrypt":
            encrypt_one_time_pad()
            break
        elif choice == "decrypt":
            decrypt_one_time_pad()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    encrypt_or_decrypt()
