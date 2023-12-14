"""
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.
"""

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return primes


Primes = sieve_of_eratosthenes(2000000)
PrimeNumbers = []
PrimeSum = 0

for i in range(len(Primes)):
    if Primes[i]:
        PrimeNumbers.append(i)

for i in range(len(PrimeNumbers)):
    PrimeSum += PrimeNumbers[i]

print(PrimeSum)
