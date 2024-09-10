def encrypt_shift_cipher(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_shift_cipher(ciphertext, shift):
    return encrypt_shift_cipher(ciphertext, -shift)

plaintext = "Nadia Mulyadi"
shift = 3
encrypted_text = encrypt_shift_cipher(plaintext, shift)
decrypted_text = decrypt_shift_cipher(encrypted_text, shift)

print(f"Plaintext: {plaintext}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
