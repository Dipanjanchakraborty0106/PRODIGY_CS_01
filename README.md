Caesar Cipher Implementation This Python program implements the Caesar Cipher algorithm, a classic encryption technique used to secure messages by shifting letters in the alphabet. Users can both encrypt and decrypt messages by specifying a shift value.

Features Encrypt plaintext messages using a specified shift value

Decrypt ciphertext messages using the same shift value

Preserves non-alphabet characters (spaces, numbers, punctuation)

Handles both uppercase and lowercase letters

User-friendly command-line interface

How the Caesar Cipher Works The Caesar Cipher is one of the simplest encryption techniques:

Each letter in the plaintext is shifted by a fixed number of positions down the alphabet

The shift value determines how many positions each character is moved

For decryption, the same shift is applied in the opposite direction

The alphabet wraps around (Z shifted by 1 becomes A)

Example with shift 3:

Plaintext: HELLO

Ciphertext: KHOOR

Requirements Python 3.x ode Structure caesar_cipher(text, shift) Function Processes each character in the input text

Shifts alphabetic characters while preserving case

Ignores non-alphabet characters

Uses modulo arithmetic for circular shifting

main() Function Handles user interaction

Collects user choices and input

Validates inputs and handles errors

Calls the cipher function with appropriate parameters

Example text Do you want to encrypt or decrypt? (e/d): e Enter the message: Hello, World! Enter the shift value: 3 Result: Khoor, Zruog! text Do you want to encrypt or decrypt? (e/d): d Enter the message: Khoor, Zruog! Enter the shift value: 3 Result: Hello, World!
