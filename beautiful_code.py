#!/user/bin/python3
def factorial(n):
    """
    
    Calculates the factorial of a given number.

    Args:
    n (int): A positive integer.

    Returns:
    int: The factorial of n.

    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
