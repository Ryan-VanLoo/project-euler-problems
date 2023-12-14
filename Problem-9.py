"""
Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists exactly one Pythagorean triplet for which
a + b + c = 1000. Find the product abc.
"""

def pythagorean_triplet():
    for a in range(1, 332):
        for b in range(a + 1, 499):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return "a =  " + str(a) + " < b = " + str(b) + " < c = " + str(c) + ", " \
                        "a + b + c = " + str(a+b+c) + " and the product (abc) is: " + str(a * b * c)


print(pythagorean_triplet())
