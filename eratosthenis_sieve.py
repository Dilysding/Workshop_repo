# This function generates prime numbers up to a user specified maximum `N`.
# The algorithm used is the Sieve of Eratosthenes.
# It is quite simple. Given an array of integers from 1 to `N`, cross out all multiples
# of 2. Find the next uncrossed integer, and cross out all of its multiples.
# Repeat until you have passed the square root of `N`.
# The uncrossed numbers that remain are all the primes less than `N`.

# quick notice: this is a verbatic port of a Java code to Python,
# and as such it is unreasonably low level.
import numpy as np

def judge_prime(Num,array):
    for i in range(np.int(np.sqrt(Num) + 1)):
            if array[i]:  # if i is uncrossed, cross its multiples
                for j in range(i**2, N, i):
                    array[j] = False  # multiple is not a prime
    return array

def eratosthenis_sieve(N):
    if N >= 2:  # the only valid case
        # Declerations:
        # initialize array to true
        arr = np.ones(N, dtype=bool)

        # get rid of known non-primes
        arr[:2] = False

        # sieve
        arr = judge_prime(Num,array)

        # how many primes are there
        prime_num = 0
        for i in range(N):
            if arr[i]:
                prime_num += 1

        primes = np.zeros(prime_num)

        # move the primes into the result
        j = 0
        for i in range(N):
            if arr[i]:  # if prime
                primes[j] = i
                j += 1
        return primes  # return the primes
    else:  # if N < 2
        return np.empty(0)  # return null array if bad imput


def test_primes():
    assert 0 not in eratosthenis_sieve(10), "0 is not a prime."
    assert 1 not in eratosthenis_sieve(10), "1 is not a prime."
    assert len(eratosthenis_sieve(10)) == 4, "There are four primes until 10."
    assert len(eratosthenis_sieve(100)) == 25, "There are 25 primes until 100."


if __name__ == "__main__":
    print(eratosthenis_sieve(10))