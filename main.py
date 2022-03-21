"""
Given a number as input, print Fizz if n is divisible by 5, Buzz if n is divisible by 3, FizzBuzz if it is divisible by 15, otherwise print the number.
Input-> 125
Output-> Buzz
"""

def func(n):
  if (n%5)==0:
    return "Fizz"
  elif (n%3)==0:
    return "Buzz"
  elif (n%15)==0:
    return "FizzBuzz"
  else:
    return "Nothing"

num = 125
print(func(num))