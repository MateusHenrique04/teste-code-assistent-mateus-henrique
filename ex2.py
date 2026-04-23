from typing import Iterable, Tuple


def calculate_statistics(values: Iterable[float]) -> Tuple[float, float, float, float]:
    """Return total, average, maximum, and minimum for the given values."""
    values_list = list(values)
    if not values_list:
        raise ValueError("The input list must contain at least one value.")

    total = sum(values_list)
    average = total / len(values_list)
    maximum = max(values_list)
    minimum = min(values_list)
    return total, average, maximum, minimum


def main() -> None:
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(numbers)

    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)


if __name__ == "__main__":
    main()