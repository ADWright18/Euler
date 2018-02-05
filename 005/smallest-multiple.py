# Author: Adomous Wright
# Problem 005

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Make it look better

smallest = 1
master_primes = []

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

for i in range(1,21):
    current_prime = prime_factor(i)

    for prime in current_prime:
        if prime in master_primes:
            if master_primes.count(prime) < current_prime.count(prime):
                add_prime = current_prime.count(prime) - master_primes.count(prime)
                print(str(add_prime))

                for i in range(0, add_prime):
                    master_primes.append(prime)
        else:
            for i in range(0, current_prime.count(prime)):
                master_primes.append(prime)

master_primes.sort()
print('Master Prime List: ' + str(master_primes))
for prime in master_primes:
    smallest *= prime

print('The smallest multiple of all numbers 1-20: ' + str(smallest))
