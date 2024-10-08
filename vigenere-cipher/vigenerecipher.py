def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return "".join(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def enkripsi_vigenere(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        x += ord('A')  
        ciphertext.append(chr(x))
    return "".join(ciphertext)

def dekripsi_vigenere(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')  
        plaintext.append(chr(x))
    return "".join(plaintext)

if __name__ == "__main__":
    plaintext = input("Masukkan plaintext: ").upper()
    key = input("Masukkan key: ").upper()

    full_key = generate_key(plaintext, key)

    encrypted_text = enkripsi_vigenere(plaintext, full_key)
    print("Hasil Enkripsi (Ciphertext):", encrypted_text)

    decrypted_text = dekripsi_vigenere(encrypted_text, full_key)
    print("Hasil Dekripsi (Plaintext):", decrypted_text)
