from PIL import Image

def encrypt_image(image_path, key, output_path):
    """
    Encrypts an image by manipulating pixel values.

    Args:
        image_path (str): Path to the input image.
        key (int): Encryption key (integer).
        output_path (str): Path to save the encrypted image.
    """
    try:
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        # Encrypt each pixel using the key
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        # Save the encrypted image
        image.save(output_path)
        print(f"Encrypted image saved to: {output_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(image_path, key, output_path):
    """
    Decrypts an image by reversing the pixel manipulation.

    Args:
        image_path (str): Path to the encrypted image.
        key (int): Decryption key (integer).
        output_path (str): Path to save the decrypted image.
    """
    try:
        # Open the encrypted image
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        # Decrypt each pixel using the key
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        # Save the decrypted image
        image.save(output_path)
        print(f"Decrypted image saved to: {output_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    """
    Main menu to handle encryption and decryption options.
    """
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")

    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            image_path = input("Enter the path to the image: ")
            key = int(input("Enter the encryption key (integer): "))
            output_path = input("Enter the output path for the encrypted image: ")
            encrypt_image(image_path, key, output_path)
        elif choice == "2":
            image_path = input("Enter the path to the encrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            output_path = input("Enter the output path for the decrypted image: ")
            decrypt_image(image_path, key, output_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
