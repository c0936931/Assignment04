def generate_fibonacci(n=20):
    a = 0
    b = 1
    sequence = []
    for _ in range(n):
        sequence.append(str(a))
        c = a
        a = b
        b = c + b
    return sequence
