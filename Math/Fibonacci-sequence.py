import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

# Change the value of 'num_terms' to generate a different number of terms
num_terms = 10
fib_sequence = fibonacci_sequence(num_terms)

# Visualize the Fibonacci sequence
plt.bar(range(1, num_terms + 1), fib_sequence)
plt.xlabel("Term")
plt.ylabel("Value")
plt.title(f"Fibonacci Sequence with {num_terms} Terms")
plt.show()
