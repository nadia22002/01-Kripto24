import numpy as np
from sympy import Matrix

# Fungsi untuk menghitung modulo matriks
def matrix_modulo(matrix, mod):
    return np.mod(matrix, mod)

# Fungsi untuk menghitung invers matriks dalam modulo tertentu
def matrix_invers(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  # Determinan matriks
    det_inv = pow(det, -1, mod)  # Invers determinan dalam modulo 26
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)  # Matriks adjugate
    inverse = matrix_modulo(det_inv * adjugate, mod)  # Matriks invers mod 26
    return inverse

# Fungsi untuk enkripsi Hill Cipher
def enkripsi_hill_cipher(plaintext, key):
    key_matrix = np.array(key)  # Konversi kunci ke matriks numpy
    n = key_matrix.shape[0]
    
    # Jika panjang plaintext tidak habis dibagi ukuran kunci, tambahkan 'X'
    if len(plaintext) % n != 0:
        padding = n - (len(plaintext) % n)
        plaintext += 'X' * padding
    
    # Konversi plaintext menjadi angka
    plaintext_matrix = [ord(char) - ord('A') for char in plaintext]
    
    # Ubah menjadi bentuk matriks
    plaintext_matrix = np.array(plaintext_matrix).reshape(-1, n).T
    
    # Lakukan enkripsi (perkalian matriks dan mod 26)
    ciphertext_matrix = matrix_modulo(np.dot(key_matrix, plaintext_matrix), 26)
    
    # Konversi kembali hasilnya menjadi teks
    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_matrix.T.flatten())
    return ciphertext

# Fungsi untuk dekripsi Hill Cipher
def dekripsi_hill_cipher(ciphertext, key):
    key_matrix = np.array(key)
    n = key_matrix.shape[0]
    
    # Konversi ciphertext menjadi angka
    ciphertext_matrix = [ord(char) - ord('A') for char in ciphertext]
    
    # Ubah menjadi bentuk matriks
    ciphertext_matrix = np.array(ciphertext_matrix).reshape(-1, n).T
    
    # Cari invers dari matriks kunci
    key_inv = matrix_invers(key_matrix, 26)
    
    # Lakukan dekripsi (perkalian dengan invers kunci dan mod 26)
    plaintext_matrix = matrix_modulo(np.dot(key_inv, ciphertext_matrix), 26)
    
    # Konversi kembali hasilnya menjadi teks
    plaintext = ''.join(chr(num + ord('A')) for num in plaintext_matrix.T.flatten())
    return plaintext

# Fungsi untuk menemukan kunci dari plaintext dan ciphertext
def cari_kunci(plaintext, ciphertext):
    n = int(np.sqrt(len(plaintext)))
    
    # Konversi plaintext dan ciphertext menjadi angka
    plaintext_matrix = np.array([ord(char) - ord('A') for char in plaintext]).reshape(n, -1)
    ciphertext_matrix = np.array([ord(char) - ord('A') for char in ciphertext]).reshape(n, -1)
    
    # Cari invers matriks plaintext (modulo 26)
    plaintext_matrix_sympy = Matrix(plaintext_matrix.T)  # Konversi ke Matrix sympy
    
    det = int(plaintext_matrix_sympy.det())  # Hitung determinan
    
    # Cek apakah determinan memiliki invers di modulo 26
    if np.gcd(det, 26) != 1:
        print(f"Matriks tidak dapat dibalik karena determinan {det} tidak memiliki invers modulo 26.")
        return None
    
    try:
        plaintext_matrix_inv = np.array(plaintext_matrix_sympy.inv_mod(26)).astype(int)
    except ValueError:
        print("Invers tidak dapat dihitung (matriks tidak dapat dibalik)")
        return None
    
    # Cari matriks kunci dengan mengalikan ciphertext dengan invers plaintext
    key_matrix = (np.dot(ciphertext_matrix.T, plaintext_matrix_inv) % 26).astype(int)
    
    return key_matrix

# Fungsi utama
def main():
    print("Program Hill Cipher")
    print("Pilihan:")
    print("e - Enkripsi")
    print("d - Dekripsi")
    print("h - Cari Kunci Hill Cipher")
    
    choice = input("Masukkan Pilihan (e/d/h): ").strip().lower()
    
    if choice == 'e':
        plaintext = input("Masukkan Plaintext: ").upper().replace(" ", "")
        key = input("Masukkan Matriks (contoh: 1,2,3,4,...): ")
        key = list(map(int, key.split(',')))
        key_size = int(len(key) ** 0.5)
        key_matrix = np.array(key).reshape(key_size, key_size)
        ciphertext = enkripsi_hill_cipher(plaintext, key_matrix)
        print(f"Hasil Enkripsi: {ciphertext}")
    
    elif choice == 'd':
        ciphertext = input("Masukkan Ciphertext: ").upper().replace(" ", "")
        key = input("Masukkan Matriks (contoh: 1,2,3,4,...): ")
        key = list(map(int, key.split(',')))
        key_size = int(len(key) ** 0.5)
        key_matrix = np.array(key).reshape(key_size, key_size)
        plaintext = dekripsi_hill_cipher(ciphertext, key_matrix)
        print(f"Hasil Dekripsi: {plaintext}")
    
    elif choice == 'h':
        plaintext = input("Masukkan Plaintext (sesuai dengan panjang ciphertext): ").upper().replace(" ", "")
        ciphertext = input("Masukkan Ciphertext: ").upper().replace(" ", "")
        key = cari_kunci(plaintext, ciphertext)
        if key is not None:
            print(f"Kunci Hill Cipher:\n{key}")
    
    else:
        print("Pilihan Invalid.")

if __name__ == "__main__":
    main()
