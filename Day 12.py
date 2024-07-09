def fibonacci_recursive(n):
    # Base case: return n if n is 0 or 1
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the previous two Fibonacci numbers
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage
n = 10  # Number of terms in the Fibonacci series
fib_series = [fibonacci_recursive(i) for i in range(n)]
print(fib_series)  # Print the Fibonacci series
