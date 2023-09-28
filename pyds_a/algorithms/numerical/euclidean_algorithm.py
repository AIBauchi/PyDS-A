"""
Author: matt-wisdom

euclidean_algorithm.py - A Python implementation of the Euclidean Algorithm for 
finding the Greatest Common Divisor (GCD) of two numbers.

The Euclidean Algorithm is an efficient method for finding the GCD of two integers. 
It works by repeatedly applying the modulo operation until the remainder becomes zero. 
The GCD is the last non-zero remainder.

Resources used:
- https://en.wikipedia.org/wiki/Euclidean_algorithm

For doctests run the following command:
python3 -m doctest -v euclidean_algorithm.py

For manual testing run:
python3 euclidean_algorithm.py
"""


def gcd(a, b):
    """
    Find the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of the two integers.

    Examples:
    >>> gcd(48, 18)
    6

    >>> gcd(60, 48)
    12
    """
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    import doctest

    doctest.testmod()
