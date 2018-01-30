# Author: Adomous Wright
# Problem 003

# What is the largest prime factor of the number 600851475143?

def prime_factor(x):
    primes = []
    d = 2
    while x > 1:
        while x % d == 0:
            primes.append(d)
            print('Added: ' + str(d))
            x /= d
        d += 1

    return primes

factors = prime_factor(600851475143)
largest_prime_factor = max(factors)

print('The largest prime factor of 600851475143: ' + str(largest_prime_factor))
