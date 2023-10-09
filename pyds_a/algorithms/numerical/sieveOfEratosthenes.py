"""
Author: prernamittal

sieve_of_eratosthenes.py - A Python implementation of the Sieve of Eratosthenes algorithm for 
generating prime numbers up to a given limit.

The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified limit.
It eliminates multiples of each prime, leaving behind only the prime numbers.

For doctests run the following command:
python3 -m doctest -v sieve_of_eratosthenes.py

For manual testing run:
python3 sieve_of_eratosthenes.py
"""

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

    Parameters:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to the specified limit.

    Examples:
    >>> sieve_of_eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
