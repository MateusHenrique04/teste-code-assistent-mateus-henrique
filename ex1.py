# ex1.py

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    for value in [1, 2, 3, 4, 17, 18, 19, 20]:
        print(f"{value} is prime: {is_prime(value)}")

