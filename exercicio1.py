def is_prime(number: int) -> bool:
    """Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        number: The integer to check for primality.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        TypeError: If number is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 2:
        return False

    if number in (2, 3):
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for factors from 5 onwards, skipping even numbers and multiples of 3
    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6

    return True