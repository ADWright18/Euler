# Author: Adomous Wright
# Problem 002

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

even_fib = []
current_fib = 0
fib_list = []
sum_fib = 0

def fibonacci(element):
    if element <= 1:
        return 1
    else:
        return fibonacci(element-2) + fibonacci(element-1)

while current_fib < 4000000:
    current_fib = fibonacci(len(fib_list))
    fib_list.append(current_fib)
    print(str(current_fib))

    if current_fib % 2 == 0:
        even_fib.append(current_fib)
        print('Added: ' + str(current_fib))

for num in even_fib:
    sum_fib += num

print('The sum of the even-valued fibonacci terms that do not exceed four million: ' + str(sum_fib))
