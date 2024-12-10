def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    Args:
        text (str): The input text to process.
        shift (int): The shift value to apply.
        mode (str): Either "encrypt" or "decrypt".

    Returns:
        str: The processed text (encrypted or decrypted).
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            # Calculate new character and wrap using modulo
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


def main():
    """
    Main function to handle user interaction and perform encryption or decryption
    based on the Caesar Cipher algorithm.
    """
    print("Welcome to the Caesar Cipher Program!")
    while True:
        mode = input("Choose an option (encrypt/decrypt/exit): ").lower()
        if mode == "exit":
            print("Goodbye!")
            break
        elif mode in ["encrypt", "decrypt"]:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
            except ValueError:
                print("Shift value must be an integer. Please try again.")
                continue

            result = caesar_cipher(message, shift, mode)
            print(f"Result ({mode}ed): {result}")
        else:
            print("Invalid option. Please choose 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
