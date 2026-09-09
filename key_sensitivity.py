import numpy as np
import matplotlib.pyplot as plt

def generate_logistic_map(seed, iterations, r=3.99):
    """Generates a discrete chaotic trajectory using the Logistic Map."""
    x = seed
    stream = np.zeros(iterations)
    for i in range(iterations):
        x = r * x * (1 - x)
        stream[i] = x
    return stream

def calculate_avalanche_effect():
    # 1. Define an original piece of data (Simulating a data block of 500 characters/bytes)
    data_length = 500
    np.random.seed(101)
    original_data = np.random.randint(0, 256, size=data_length, dtype=np.uint8)
    
    # 2. Encrypt using the Exact Master Key
    master_key = 0.123456789012345
    chaos_source = generate_logistic_map(seed=master_key, iterations=data_length)
    key_mask = (chaos_source * 100000).astype(np.uint8)
    ciphertext = np.bitwise_xor(original_data, key_mask)
    
    # 3. Define a microscopic deviation to test an unauthorized user (Eve)
    # We alter the 15th decimal place by adding just 0.000000000000001
    altered_key = master_key + 1e-15
    
    # 4. Attempt decryption with the wrong key
    wrong_chaos_source = generate_logistic_map(seed=altered_key, iterations=data_length)
    wrong_key_mask = (wrong_chaos_source * 100000).astype(np.uint8)
    decryption_attempt = np.bitwise_xor(ciphertext, wrong_key_mask)
    
    # 5. Evaluate the Avalanche Effect (How many bits actually changed?)
    # Convert arrays to binary strings to compare individual bit transitions
    original_bits = np.unpackbits(original_data)
    failed_bits = np.unpackbits(decryption_attempt)
    
    # Count how many total bits are different between original data and failed decryption
    bit_differences = np.sum(original_bits != failed_bits)
    avalanche_percentage = (bit_differences / len(original_bits)) * 100
    
    # --- DISPLAY METRICS IN TERMINAL ---
    print("\n" + "="*55)
    print("🔒 CRYPTOGRAPHIC AVALANCHE EFFECT ANALYSIS")
    print("="*55)
    print(f"Master Key (Alice):  {master_key:.15f}")
    print(f"Altered Key (Eve):   {altered_key:.15f}")
    print(f"Mathematical Delta:  1e-15 (Absolute minimum floating boundary)")
    print("-"*55)
    print(f"Total Bits Analyzed: {len(original_bits)} bits")
    print(f"Corrupted Bits:      {bit_differences} bits")
    print(f"Avalanche Metric:    {avalanche_percentage:.2f}%")
    print("-"*55)
    
    if 45.0 <= avalanche_percentage <= 55.0:
        print("✅ PASS: Ideal Avalanche Effect achieved (~50%).\n"
              "         An attacker cannot extract fractional hints from near-guesses.")
    else:
        print("❌ FAIL: Weak key sensitivity. Algorithm needs scaling.")
    print("="*55 + "\n")

    # 6. Plot the trajectory divergence to visually prove the chaos to your advisors
    plt.figure(figsize=(12, 5))
    plt.plot(chaos_source[:50], label=f"Master Key ({master_key})", color='blue', linewidth=1.5)
    plt.plot(wrong_chaos_source[:50], label=f"Altered Key ({altered_key})", color='red', linestyle='--', linewidth=1.5)
    plt.title("Key Sensitivity: Microscopic Input Divergence Over Time Steps")
    plt.xlabel("Iteration Step (n)")
    plt.ylabel("Chaotic State Value (x)")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle=':')
    plt.show()

# Run the analyzer engine
calculate_avalanche_effect()
