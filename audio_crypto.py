import os
import numpy as np
from scipy.io import wavfile

def generate_chaos_keys(seed, iterations, r=3.99):
    x = seed
    keys = []
    for _ in range(iterations):
        x = r * x * (1 - x)
        keys.append(x)
    return keys

def process_audio_file(input_wav_path, encrypted_out_path, decrypted_out_path, secret_key):
    # Check if sample file exists
    if not os.path.exists(input_wav_path):
        print(f"🛑 Error: Could not find '{input_wav_path}' in your folder!")
        print("Please drag and drop a standard .wav audio track into your project directory first.")
        return

    # 1. Read the audio waves from disk
    sample_rate, data = wavfile.read(input_wav_path)
    
    # Store original alignment dimensions (Mono vs Stereo audio tracks)
    original_shape = data.shape
    flat_data = data.flatten()
    total_samples = len(flat_data)
    
    print(f"🎵 Audio file loaded successfully! Total samples to encrypt: {total_samples}")
    print("🔄 Spawning mathematical chaotic sequence stream... Please wait...")
    
    # 2. Generate a chaotic element matrix exactly matching data length
    chaos_floats = generate_chaos_keys(seed=secret_key, iterations=total_samples)
    
    # Scale float decimals into integer limits that safely match audio properties
    chaos_mask = (np.array(chaos_floats) * 100000).astype(flat_data.dtype)
    
    # 3. Encryption Phase (XOR logic masks sound channels)
    print("🔒 Scrambling signal lines into white noise...")
    encrypted_flat = np.bitwise_xor(flat_data, chaos_mask)
    encrypted_data = encrypted_flat.reshape(original_shape)
    
    # Save the unlistenable noisy audio file
    wavfile.write(encrypted_out_path, sample_rate, encrypted_data)
    print(f"✅ Encrypted file written as: '{encrypted_out_path}'")

    # 4. Decryption Phase (XOR inversion unmasks original parameters)
    print("🔓 Executing matched mirror inverse decoding pass...")
    decrypted_flat = np.bitwise_xor(encrypted_flat, chaos_mask)
    decrypted_data = decrypted_flat.reshape(original_shape)
    
    # Save the completely recovered sound file
    wavfile.write(decrypted_out_path, sample_rate, decrypted_data)
    print(f"✅ Decrypted file recovered cleanly as: '{decrypted_out_path}'")

# --- EXECUTION ROOT ROUTINE ---
# Configuration paths
input_track = "sample.wav" 
encrypted_track = "encrypted_output.wav"
decrypted_track = "recovered_output.wav"
my_master_key = 0.543210

process_audio_file(input_track, encrypted_track, decrypted_track, my_master_key)
