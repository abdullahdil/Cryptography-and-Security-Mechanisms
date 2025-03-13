import time
import itertools

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def rail_fence_decrypt(ciphertext, rails):
    if rails < 2:
        return ciphertext

    rail_pattern = list(itertools.cycle(list(range(rails)) + list(range(rails - 2, 0, -1))))
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    idx_order = sorted(range(len(ciphertext)), key=lambda i: rail_pattern[i])

    idx = 0
    for row in range(rails):
        for i in idx_order:
            if rail_pattern[i] == row:
                fence[row][i] = ciphertext[idx]
                idx += 1

    return ''.join(''.join(row) for row in fence)

def brute_force_caesar(ciphertext):
    print("\nCaesar Cipher Brute Force:")
    start_time = time.time()
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")

def brute_force_rail_fence(ciphertext, max_rails=10):
    print("\nRail Fence Cipher Brute Force:")
    start_time = time.time()
    for rails in range(2, max_rails + 1):
        decrypted_text = rail_fence_decrypt(ciphertext, rails)
        print(f"Rails {rails}: {decrypted_text}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")

def brute_force_product_cipher(ciphertext, max_rails=10):
    print("\nProduct Cipher Brute Force:")
    start_time = time.time()
    for shift in range(26):
        caesar_decrypted = caesar_cipher_decrypt(ciphertext, shift)
        for rails1 in range(2, max_rails + 1):
            first_rail_decrypted = rail_fence_decrypt(caesar_decrypted, rails1)
            for rails2 in range(2, max_rails + 1):
                final_decrypted = rail_fence_decrypt(first_rail_decrypted, rails2)
                print(f"Shift {shift}, Rails {rails1}, Rails {rails2}: {final_decrypted}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")

# Example usage
ciphertext_product = "Koroh"

brute_force_product_cipher(ciphertext_product)
