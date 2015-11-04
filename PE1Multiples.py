#!/usr/bin/env python
"""
Problem 1:

* Add all the natural numbers below 1000 that are multiples of 3 or 5.

Modifications:

* The two factors and highest number are variables and can be changed.

* An array is used instead of a generator so that the
contents may be viewed or altered at any time.

"""
__author__ = "Nick Irwin"
__version__ = "1.0"
__email__ = "nick980@wowway.com"

def sumMultiples(factor1, factor2, low, high):
    multiples = []
    for i in range (low, high):
        if i%factor1 == 0 or i%factor2 == 0:
            #Store i within array
            multiples.append(i)
            
    b = sum(multiples)
    print (b)

sumMultiples(3, 5, 0, 1000)
