import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

def golden_ratio_approximation(sequence):
    ratios = [sequence[i+1] / sequence[i] if sequence[i] != 0 else 0 for i in range(len(sequence)-1)]
    return ratios

# Change the value of 'num_terms' to generate a different number of terms
num_terms = 11
fib_sequence = fibonacci_sequence(num_terms)
golden_ratios = golden_ratio_approximation(fib_sequence)

# Visualize the Fibonacci sequence and golden ratio approximation
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_terms), golden_ratios, marker='o', label="Golden Ratio Approximation")
plt.axhline(y=(1 + 5 ** 0.5) / 2, color='r', linestyle='--', label="Actual Golden Ratio")
plt.xlabel("Term")
plt.ylabel("Ratio")
plt.title(f"Fibonacci Sequence and Golden Ratio Approximation with {num_terms-1} Terms")
plt.legend()
plt.show()
