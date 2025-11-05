# Fizz Buzz using a dictionary April, 9, 2020

def generate_fizzbuzz(n=100):
    vals = {"Fizz": 3, "Buzz": 5}  # Define multiples to be used

    results = []
    for i in range(1, n + 1):
        out = ""
        for key in vals:
            if i % vals[key] == 0:
                out += key
        if not out:
            out = str(i)
        results.append(out)
    return results
