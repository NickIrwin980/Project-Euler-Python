#!/usr/bin/env python
"""

Problem 2:

* By considering the terms in the Fibonacci sequence whose values do not
  exceed four million, find the sum of the even-valued terms.

"""
__author__ = "Nick Irwin"
__version__ = "1.0"
__email__ = "nick980@wowway.com"
def sumOfEvenTerms(prev=1):
    
    #prev is the value behind the highest calculated value in the Fibonacci sequence
    #newNext is the current highest calculated value in the Fibonacci sequence
    newNext = 1
    
    #oldNext is used to update prev 
    oldNext = 0
    while newNext <= 4000000:
        oldNext = newNext
        newNext = newNext + prev
        prev = oldNext
        if not newNext%2:
            yield newNext
        
print (sum(sumOfEvenTerms()))
