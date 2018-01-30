# Author: Adomous Wright
# Problem 001

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

multiples = []
sum_multiples = 0


for i in range(0,1000):
    if i % 3 == 0:
        multiples.append(i)
        continue
    elif i % 5 == 0:
        multiples.append(i)
        continue

for num in multiples:
    sum_multiples += num

print('The sum of the multiples of 3 and 5 from 0 to 1000: ' + str(sum_multiples)) 
