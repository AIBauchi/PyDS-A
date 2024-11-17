"""
Author: Avijit-Dey

longest_common_subsequence.py - A Python implementation of Longest Common Subsequence,
a famous problem in Dynamic Programming.

A longest common subsequence (LCS) is the longest subsequence common to all sequences
in a set of sequences (often just two sequences). It differs from the longest common
substring: unlike substrings, subsequences are not required to occupy consecutive
positions within the original sequences. The problem of computing longest common 
subsequences is a classic computer science problem, the basis of data comparison
programs such as the diff utility, and has applications in computational linguistics
and bioinformatics. It is also widely used by revision control systems such as Git for
reconciling multiple changes made to a revision-controlled collection of files. 

Resources used:
--https://en.wikipedia.org/wiki/Longest_common_subsequence

For doctests run the following command:
python3 -m doctest -v longest_common_subsequence.py (linux/unix)
python -m doctest -v longest_common_subsequence.py (windows)

For manual testing run:
python3 longest_common_subsequence.py (linux/unix)
python longest_common_subsequence.py (windows)
"""


def longest_common_subsequence(first_string, second_string):
    """

    Examples:
    >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
    4
    >>> longest_common_subsequence("AAAAAA", "GGGGGG")
    0
    >>> longest_common_subsequence("ROFLABU", "DAFLADBU")
    5
    """
    # length of the strings
    len_first_str = len(first_string)
    len_secong_str = len(second_string)

    # declaring the lookup table list for storing the values
    lookup_table = [[0] * (len_secong_str + 1) for i in range(len_first_str + 1)]

    # Following steps build in bottom up fashion:
    for i in range(len_first_str + 1):
        for j in range(len_secong_str + 1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif first_string[i - 1] == second_string[j - 1]:
                lookup_table[i][j] = lookup_table[i - 1][j - 1] + 1
            else:
                lookup_table[i][j] = max(lookup_table[i - 1][j], lookup_table[i][j - 1])

    # return the length of the longest common subsequence
    return lookup_table[len_first_str][len_secong_str]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
