def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Please input integers only")
    if n < 0:
        raise ValueError("Please enter a non-negative number")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
