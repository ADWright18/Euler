# Author: Adomous Wright
# Problem 007

# What is the 10001st prime number?

import math

primes = []
x = 0;

while len(primes) < 10001:

    x += 1

    if len(primes) == 0:
        primes.append(1)
        print('Added: ' + str(x))
        print('Number of Primes; ' + str(len(primes)))

    elif len(primes) == 1:
        primes.append(2)
        print('Added: ' + str(x))
        print('Number of Primes; ' + str(len(primes)))

    else:
        for prime in primes:
            if prime == 1:
                continue
            elif x % prime == 0:
                break
            elif prime > math.sqrt(x):
                primes.append(x)
                print('Added: ' + str(x))
                print('Number of Primes; ' + str(len(primes)))
                break
            elif primes.index(prime) == len(primes) - 1:
                primes.append(x)
                print('Added: ' + str(x))
                print('Number of Primes; ' + str(len(primes)))
                break

print('10001st Prime Number: ' + str(x))
