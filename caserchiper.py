import os
def caesar_encrypt(text, shift, mode="alpha"):
    if mode == "ascii":
        return " ".join(str((ord(char) + shift) % 256) for char in text)
    else:
        encrypted = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
        return encrypted
def caesar_decrypt(text, shift, mode="alpha"):
    if mode == "ascii":
        try:
            # Auto-detect: if text is space-separated numbers, decode them
            ascii_numbers = [int(num) for num in text.strip().split()]
            return ''.join(chr((num - shift) % 256) for num in ascii_numbers)
        except ValueError:
            return "[ERROR] ASCII decryption failed. Expected space-separated numbers."
    else:
        return caesar_encrypt(text, -shift, mode)
def get_shift():
    while True:
        try:
            return int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid input. Please enter a number. ")
def get_text_input():
    while True:
        choice = input("Use(T)ext input or (F)ile input?: ").strip().upper()
        if choice == "F":
            path = input("Enter file path:").strip('" ')
            if not os.path.exists(path):
                print("File not found.")
                continue
            with open(path, "r", encoding="utf-8") as f:
                return f.read().strip(), path
        elif choice == "T":
            return input("Enter the message: "), None
        else:
            print("Invalid choice. Use 'T' or 'F'.")
def save_output(text, mode):
    choice = input("Do you want to save the output? (Y/N): ").strip().upper()
    if choice == "Y":
        path = input("Enter filename to save (e.g. result.txt): ").strip()
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Output saved to {path}")
def choose_mode():
    while True:
        mode = input("Use (A)lphabetic mode or (B)yte ASCII mode?: ").strip().upper()
        if mode == "A":
            return "alpha"
        elif mode == "B":
            return "ascii"
        else:
            print("Invalid mode. Choose A or B.")
def main():
    print("=== Advanced Caesar Cipher ===")
    while True:
        print("\nMenu:")
        print("1 Encrypt Message")
        print("2 Decrypt Message")
        print("3 Exit")
        choice = input("👉 Choose an option (1-3): ").strip()
        if choice == '1':
            text, _ = get_text_input()
            shift = get_shift()
            mode = choose_mode()
            result = caesar_encrypt(text, shift, mode)
            print(f"\nEncrypted Message:\n{result}")
            save_output(result, mode)
        elif choice == '2':
            text, _ = get_text_input()
            shift = get_shift()
            mode = choose_mode()
            result = caesar_decrypt(text, shift, mode)
            print(f"\nDecrypted Message:\n{result}")
            save_output(result, mode)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")
if __name__ == "__main__":
    main()