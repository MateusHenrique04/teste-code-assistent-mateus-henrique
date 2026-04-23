# ex1.py

from math import isqrt


def is_prime(number: int) -> bool:
    """Return True if `number` is a prime integer, otherwise False."""
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2

    limit = isqrt(number)
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


def main() -> None:
    numbers = [1, 2, 3, 4, 17, 18, 19, 20]
    for value in numbers:
        print(f"{value} is prime: {is_prime(value)}")


if __name__ == "__main__":
    main()
