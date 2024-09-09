from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    # Open image and convert to numpy array
    image = Image.open(input_path)
    pixels = np.array(image)

    # Encryption: Apply XOR operation with the key
    encrypted_pixels = pixels ^ key

    # Save encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Open image and convert to numpy array
    image = Image.open(input_path)
    pixels = np.array(image)

    # Decryption: Apply XOR operation with the key
    decrypted_pixels = pixels ^ key

    # Save decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)

def main():
    input_image_path = r'D:\Prodigy\Tasks\Task-2 input image.png'
    encrypted_image_path = r'D:\Prodigy\Tasks\encrypted_image.png'
    decrypted_image_path = r'D:\Prodigy\Tasks\decrypted_image.png'
    
    # Key for XOR operation (should be an integer between 0 and 255)
    key = 123

    # Check if the output directory exists; if not, create it
    output_directory = os.path.dirname(encrypted_image_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)
    print(f'Image encrypted and saved to {encrypted_image_path}')

    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)
    print(f'Image decrypted and saved to {decrypted_image_path}')

if __name__ == "__main__":
    main()
