"""
Project Euler - Problem 3: Largest Prime Factor
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math


def is_prime(number):
   if number < 2:
       return False
   if number == 2:
       return True
   else:
       for i in range(2, number):
           if number % i == 0:
               return False
       return True


def biggest_prime_factor(number):
    for i in reversed(range(int(math.sqrt(number)))):
        if number % i == 0 and is_prime(i):
            return i


print("The Largest Prime Factor of 600,851,475,143 is: ", biggest_prime_factor(600851475143))
