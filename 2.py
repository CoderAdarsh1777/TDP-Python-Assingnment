def generate_fibonacci(n):
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence.append(0)
    elif n == 2:
        fibonacci_sequence.extend([0, 1])
    else:
        fibonacci_sequence.extend([0, 1])
        a, b = 0, 1
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
    return fibonacci_sequence

def main():
    n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    
    fibonacci_sequence = generate_fibonacci(n)
    
    print("Fibonacci Sequence:")
    for num in fibonacci_sequence:
        print(num, end=" ")

if __name__ == "__main__":
    main()
