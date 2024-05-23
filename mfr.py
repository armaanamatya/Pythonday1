#[map] Create a function convert_to_uppercase that takes a list of strings as input and uses the map function 
# to return a new list with all the strings converted to uppercase.

def convert_to_uppercase(stings):
        upper = list(map(lambda x : x.upper(), strings))
        return upper
    
strings = ["armaan", "time", "random"]
upper = convert_to_uppercase(strings)
print(upper)

#[filter] Implement a function called filter_prime_numbers that takes a list of integers as input 
# and uses the filter function to return a new list containing only the prime numbers.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime_numbers(nums):
    filtered = list(filter(lambda x : is_prime(x), nums))
    return filtered

nums = [1,5,8,9,11,13]
filtered = filter_prime_numbers(nums)
print(filtered)

#[reduce] Write a Python function calculate_factorial that takes an integer as input and uses the reduce function to return the factorial of that number.
from functools import reduce

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        nums = range(1,n+1)
        fact = reduce((lambda x,y: x * y), nums)
    
    return fact

fact = calculate_factorial(5)
print(fact) 