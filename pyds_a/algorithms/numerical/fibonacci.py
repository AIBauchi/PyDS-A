# Function to calculate the n-th Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Fibonacci numbers are calculated recursively
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example of usage:
n = 10
print(f"The {n}th Fibonacci number is {fibonacci(n)}")
