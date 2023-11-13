"""
Project Euler - Problem 2
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def sum_even_fibonacci_numbers(limit):
    sum = 0
    a = 1
    b = 1
    c = a + b
    while c < limit:
        if c % 2 == 0:
            sum += c
        a = b
        b = c
        c = a + b
    return sum


print("The Sum of Even Fibonacci Terms Under Four Million is: ", sum_even_fibonacci_numbers(4000000))

