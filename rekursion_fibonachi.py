def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")

print_fibonacci_sequence(6)
