# Author: Adomous Wright
# Problem 006

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

a_sum = 0

square_list = []
sum_square = 0

for i in range(1,101):
    square_list.append(i**2)
    a_sum += i

for number in square_list:
    sum_square += number

square_sum = a_sum**2

sum_square_difference = square_sum - sum_square

print('Sum of squares: ' + str(sum_square))
print('Square of sum: ' + str(square_sum))
print('The difference between the sum of squares and square of the sum: ' + str(sum_square_difference))
