import numpy as np
import matplotlib.pyplot as plt

def generate_bifurcation_data():
    # 1. Generate an array of 'r' values ranging from 2.5 to 4.0
    # We use 10,000 steps to create a dense, highly detailed mathematical plot
    n_r_steps = 10000
    r_values = np.linspace(2.5, 4.0, n_r_steps)
    
    # Run 1000 total loops per 'r', but drop the first 900 
    # This discards the initial setup phase and saves only the permanent states
    iterations = 1000
    last_samples = 100
    
    # Initialize the starting point (seed) for every calculation
    x = 1e-5 * np.ones(n_r_steps)
    
    print("🧮 Calculating 10 million mathematical points... Please wait...")
    
    # Arrays to store the final coordinates for plotting
    r_plot = []
    x_plot = []
    
    # 2. Iterate through the chaotic equation loop
    for i in range(iterations):
        x = r_values * x * (1.0 - x)
        
        # If we are in the final 100 loops, record the values
        if i >= (iterations - last_samples):
            r_plot.append(r_values)
            x_plot.append(x)
            
    print("✅ Calculations complete. Generating the structural diagram...")
    
    # 3. Plot the final Bifurcation Mapping
    plt.figure(figsize=(12, 7), dpi=150)
    plt.plot(r_plot, x_plot, ',k', alpha=0.1) # ',k' draws microscopic black pixel dots
    
    # Visual markers highlighting design choices for your project review
    plt.axvline(x=3.57, color='red', linestyle='--', alpha=0.7, label='Onset of Chaos (r = 3.57)')
    plt.axvline(x=3.99, color='green', linestyle='-', alpha=0.8, linewidth=2, label='Our System Target (r = 3.99)')
    
    plt.title("Bifurcation Diagram of the Logistic Map: Proving the Chaos Region", fontsize=14)
    plt.xlabel("Control Parameter (r)", fontsize=12)
    plt.ylabel("Stable System States (x)", fontsize=12)
    plt.xlim(2.5, 4.0)
    plt.legend(loc="upper left")
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.show()

# Run the simulation engine
generate_bifurcation_data()
