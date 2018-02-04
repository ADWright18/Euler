# Author: Adomous Wright
# Problem 004

# Find the largest palindrome made from the product of two 3-digit numbers\

def isPalindrone(number):
    '''Check each digit of the number to check for a palimdrone'''
    str_number = str(number)
    digits = list(str_number)
    length = len(digits)

    for i in range(0, length):
        if digits[i] != digits[length-1-i]:
            return False
            break

    return True

largest = 0

for i in range(100,1000):

    for j in range(100,1000):

        product = i*j
        if isPalindrone(product) and product > largest:
            print("The new largest palindrome: " + str(product))
            largest = product

print("The largest palindrome is: " + str(largest))
