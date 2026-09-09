def generate_chaos_keys(seed, iterations, r=3.99):
    x = seed
    keys = []
    for _ in range(iterations):
        x = r * x * (1 - x)
        keys.append(x)
    return keys

def encrypt_decrypt_text(message, secret_key):
    # 1. Convert characters to their integer code values (ASCII bytes)
    plaintext_bytes = [ord(char) for char in message]
    
    # 2. Generate chaotic numbers matching the length of our message
    chaos_floats = generate_chaos_keys(seed=secret_key, iterations=len(message))
    
    # 3. Scale the decimals (0.0 to 1.0) into whole numbers (0 to 255) for bitwise operations
    chaos_integers = [int(f * 100000) % 256 for f in chaos_floats]
    
    # 4. XOR scramble step
    processed_bytes = []
    for p_byte, c_key in zip(plaintext_bytes, chaos_integers):
        processed_bytes.append(p_byte ^ c_key) # ^ is the XOR operator
        
    # Return both the raw numbers and the readable scrambled text string
    return processed_bytes, "".join([chr(b) for b in processed_bytes])

# --- SYSTEM TRIAL RUN ---
original_message = "Secure Chaos Message 2026!"
key_alice = 0.735194  # The true key shared between sender and receiver
key_eve = 0.735195    # The interceptor's guess (Off by a tiny 0.000001!)

print(f"Original Plaintext: {original_message}\n")

# Step A: Encryption
encrypted_bytes, encrypted_text = encrypt_decrypt_text(original_message, key_alice)
print(f"Scrambled Ciphertext (What goes over the air): {repr(encrypted_text)}\n")

# Step B: Decryption with CORRECT key
_, bob_decrypted = encrypt_decrypt_text(encrypted_text, key_alice)
print(f"Bob's Decryption (Using Correct Key): {bob_decrypted}")

# Step C: Decryption with INCORRECT key
_, eve_decrypted = encrypt_decrypt_text(encrypted_text, key_eve)
print(f"Eve's Decryption (Using Wrong Key): {repr(eve_decrypted)}")
