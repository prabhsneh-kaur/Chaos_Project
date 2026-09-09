import time
import matplotlib.pyplot as plt

def generate_chaos_keys(seed, iterations, r=3.99):
    x = seed
    keys = []
    for _ in range(iterations):
        x = r * x * (1 - x)
        keys.append(x)
    return keys

# Generate 100 chaotic numbers using our secret key
secret_seed = 0.456789
print("Generating chaotic wave...")
chaos_stream = generate_chaos_keys(seed=secret_seed, iterations=100)

# Print the first 5 numbers to the screen
print("First 5 chaotic keys:")
for i in range(5):
    print(f"Key {i}: {chaos_stream[i]:.6f}")

# Plot the graph
plt.figure(figsize=(10, 4))
plt.plot(chaos_stream, marker='o', color='purple', linestyle='-')
plt.title("Chaotic Trajectory Output")
plt.xlabel("Time Step (n)")
plt.ylabel("Chaotic State (x)")
plt.grid(True)
plt.show()
