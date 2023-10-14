"""
Author: prernamittal

miller_rabin.py - A Python implementation of the Miller-Rabin primality testing algorithm.

The Miller-Rabin algorithm is a probabilistic primality testing method. It determines whether a given number 
is likely to be prime or composite by applying a series of tests based on random numbers.

For doctests run the following command:
python3 -m doctest -v miller_rabin.py

For manual testing run:
python3 miller_rabin.py
"""

import random

def miller_rabin(n, k=5):
    """
    Perform Miller-Rabin primality testing on a given number.

    Parameters:
        n (int): The number to be tested for primality.
        k (int): The number of iterations for the Miller-Rabin test. Higher k means higher accuracy.

    Returns:
        bool: True if the number is likely to be prime, False if it's composite.

    Examples:
    >>> miller_rabin(17)
    True

    >>> miller_rabin(100)
    False
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()
